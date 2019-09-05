#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals,\
    absolute_import, division

import os
import sys
import codecs
import subprocess

#color_names = ["black", "red", "blue", "green"]
color_names = ["black", "red", "green", "blue", "yellow", "purple", "orange", "cyan"]
class Config:
    def __init__(self):
        self.elements = {}

    def load_from_file(self, filename):
        with codecs.open(filename, 'r', 'utf-8') as f:
            for line in f:
                if not line.startswith('#'):
                    ar = line.strip().split('\t')
                    if len(ar) >= 2:
                        self.elements[ar[0]] = ar[1]

    def get_bool(self, name, default_value = False):
        if name in self.elements:
            return self.elements[name] == "True" or self.elements[name] == "true"
        else:
            return default_value

    def get_int(self, name, default_value = 0):
        if name in self.elements:
            return (int)(self.elements[name])
        else:
            return default_value

    def get_float(self, name, default_value = 0.0):
        if name in self.elements:
            return (float)(self.elements[name])
        else:
            return default_value

    def get_string(self, name, default_value = ""):
        if name in self.elements:
            return self.elements[name]
        else:
            return default_value

def make_neato_file(edges, fout):
    print("graph G {", file = fout)
    for e in edges:
        print("\t{} -- {};".format(e[0], e[1]), file = fout)
    print("}", file = fout)

def make_pos_list(edges, conf):
    neato_filename = "neato_file_for_draw_subgraphs.txt"
    output_graph_filename = "output_graph_for_draw_subgraphs.txt"
    pos_filename = "pos_list_for_draw_subgraphs.txt"

    with open(neato_filename, "w") as fout:
        make_neato_file(edges, fout)
    subprocess.call(["neato", neato_filename, "-Tplain", "-o",
                     output_graph_filename])
    nodes = {}
    with open(output_graph_filename) as f:
        for line in f:
            ar = line.strip().split()
            if ar[0] == "node":
                nodes[int(ar[1])] = [float(ar[2]), float(ar[3])]
    min_x = min([nodes[n][0] for n in nodes])
    min_y = min([nodes[n][1] for n in nodes])
    # make all the positions positive
    if min_x < 0:
        for n in nodes:
            nodes[n][0] -= min_x
    if min_y < 0:
        for n in nodes:
            nodes[n][1] -= min_y

    max_x = max([nodes[n][0] for n in nodes])
    max_y = max([nodes[n][1] for n in nodes])

    ra = conf.get_float("WidthPerGraph", 90.0) / min(max_x, max_y)

    for n in nodes:
        nodes[n][0] *= ra
        nodes[n][1] *= ra
    with open(pos_filename, "w") as fout:
        for n in sorted(nodes.keys()):
            print("{} {}".format(int(nodes[n][0]), int(nodes[n][1])), file = fout)

def draw_graph(offset, edges, subedges, poses, conf):

    text = ""

    radius = 8

    count = 1
    for i in range(len(edges)):
        e = edges[i]
        p = poses[e[0] - 1]
        x1 = p[0] + offset[0] #<!--stroke-dasharray="5 5" -->
        y1 = p[1] + offset[1]
        p = poses[e[1] - 1]
        x2 = p[0] + offset[0]
        y2 = p[1] + offset[1]

        if subedges[i] <= 0:
            color = "black"
        else:
            color = color_names[subedges[i]]
        if subedges[i] < 0:
            swidth = 2
            opt = 'stroke-dasharray="3 3" '
        else:
            swidth = 10
            opt = ''
            
        text += '<line x1="{0}" y1="{1}" x2="{2}" y2="{3}" '.format(x1, y1, x2, y2)
        text += 'stroke="{0}" stroke-width="{1}" {2}/> '.format(color, swidth, opt)
        text += "\n"

    ctext = 1
    for p in poses:
        x = p[0] + offset[0]
        y = p[1] + offset[1]
        text += '<circle cx="{0}" cy="{1}" r="{2}" '.format(x, y, radius)
        text += 'fill="white" stroke="black" stroke-width="2" />\n'

        # vertex label
        if conf.get_bool("VertexLabel", True):
            text += '<text x="{0}" y="{1}" font-family="Times New Roman" font-size="12">{2}</text>'.format(x - 2, y + 2, ctext)

        text += "\n"
        ctext += 1

    xmax = max([p[0] for p in poses])
    ymax = max([p[1] for p in poses])
    return (text, xmax + radius, ymax + radius)

def main():

    args = sys.argv[:]

    if "--reverse" in args:
        is_reverse = True
        args.remove("--reverse")
    else:
        is_reverse = False

    if "--black" in args:
        color_names[1] = "black"
        args.remove("--black")

    if len(args) <= 2:
        print("Usage: python {0} ".format(args[0]) + \
              "<edge list> <color list> [<pos list>] [--reverse]")
        print("  --reverse   each line of the color list")
        print("  --black     set the first color to black")
        exit(0)

    edge_list_filename = args[1]
    color_list_filename = args[2]

    if len(args) >= 4: # read pos file if exists
        pos_filename = args[3]
    else: # pos file does not exist
        pos_filename = ""

    conf = Config()
    if os.path.exists("config.txt"):
        conf.load_from_file("config.txt")

    xmargin = conf.get_int("XMargin", 20)
    ymargin = conf.get_int("YMargin", 20)
    margin = (xmargin, ymargin)
    numofx = conf.get_int("NumberOfGraphsPerLine", 6)

    edges = []
    vertices = set()
    with open(edge_list_filename) as f:
        linenum = 1
        for line in f:
            ar = line.strip().split()
            if len(ar) < 2:
                print("The number of elements at Line {} ".format(linenum)
                      + "in the graph file is {}.".format(len(ar)), file = sys.stderr)
                print("It must be two.", file = sys.stderr)
                exit(1)
            edges.append((int(ar[0]), int(ar[1])))
            vertices.add(int(ar[0]))
            vertices.add(int(ar[1]))
            linenum += 1

    num_m = len(edges) # number of edges
    num_n = len(vertices) # number of vertices

    poses = []
    if pos_filename == "": # pos file does not exist
        make_pos_list(edges, conf)
        pos_filename = "pos_list_for_draw_subgraphs.txt"

    linenum = 1
    with open(pos_filename) as f:
        for line in f:
            ar = line.strip().split()
            if len(ar) < 2:
                print("The number of elements at Line {} ".format(linenum)
                      + "in the pos file is {}.".format(len(ar)), file = sys.stderr)
                print("It must be two.", file = sys.stderr)
                exit(1)
            poses.append((int(ar[0]), int(ar[1])))
            linenum += 1

    if linenum - 1 < num_n:
        print("The number of lines in the pos file"
              + " is {}.".format(linenum - 1), file = sys.stderr)
        print("It must be {}, which is the number of vertices.".format(num_n),
              file = sys.stderr)
        exit(1)

    axmax = margin[0]
    aymax = margin[1]
    astr = ""
    offset = [margin[0], margin[1]]
    count = 0

    valid_values = list(map(str, range(len(color_names))))
    with open(color_list_filename) as f:
        linenum = 1
        # draw each subgraph
        for line in f:
            ar = line.strip().split()
            for a in ar:
                if a not in valid_values:
                    print('Line {} has value "{}", but '.format(linenum, a)
                          + 'it must be 0,...,{}.'.format(len(color_names) - 1),
                          file = sys.stderr)
                    exit(1)
            subedges = list(map(int, ar))
            if is_reverse:
                subedges.reverse()
            if len(subedges) < num_m:
                print("Line {} has {} values, but ".format(linenum, len(subedges))
                      + "it must be {}, ".format(num_m)
                      + "which is the number of edges.", file = sys.stderr)
                exit(1)
            for i in range(len(subedges)):
                if subedges[i] == 0:
                    subedges[i] = -1 # convert solid line to dotted line
            (st, xmax, ymax) = draw_graph(offset, edges, subedges, poses, conf)
            if axmax < offset[0] + xmax + margin[0]:
                axmax = offset[0] + xmax + margin[0]
            if aymax < offset[1] + ymax + margin[1]:
                aymax = offset[1] + ymax + margin[1]
            offset[0] += xmax + margin[0]
            count += 1
            if count % numofx == 0:
                offset[1] += ymax + margin[1]
                offset[0] = margin[0]

            astr += st
            linenum += 1

    print('<svg xmlns="http://www.w3.org/2000/svg" ', end="")
    print('width="{0}" height="{1}">'.format(axmax + margin[0], aymax + margin[1]))
    print(astr)
    print('</svg>')

if __name__ == '__main__':
    main()
