#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals,\
    absolute_import, division

import sys
import subprocess

def make_neato_file(edges, fout):
    print("graph G {", file = fout)
    for e in edges:
        print("\t{} -- {};".format(e[0], e[1]), file = fout)
    print("}", file = fout)

def make_pos_list(edges):
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

    ra = 90.0 / min(max_x, max_y)

    for n in nodes:
        nodes[n][0] *= ra
        nodes[n][1] *= ra
    with open(pos_filename, "w") as fout:
        for n in sorted(nodes.keys()):
            print("{} {}".format(int(nodes[n][0]), int(nodes[n][1])), file = fout)

def draw_graph(offset, edges, subedges, poses):

    text = ""

    #color_names = ["black", "red", "blue", "green"]
    color_names = ["black", "red", "green", "blue"]
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
        text += '<text x="{0}" y="{1}" font-family="Times New Roman" font-size="12">'.format(x - 2, y + 2)
        text += str(ctext)
        text += '</text>'
        text += "\n"
        ctext += 1

    xmax = max([p[0] for p in poses])
    ymax = max([p[1] for p in poses])
    return (text, xmax + radius, ymax + radius)

def main():

    margin = (20, 20)
    numofx = 6

    if len(sys.argv) <= 2:
        print("Usage: python {0} ".format(sys.argv[0]) + \
              "<edge list> <color list> [<pos list>]")
        exit(0)

    edges = []
    vertices = set()
    with open(sys.argv[1]) as f:
        for line in f:
            ar = line.strip().split()
            edges.append((int(ar[0]), int(ar[1])))
            vertices.add(int(ar[0]))
            vertices.add(int(ar[1]))

    num_m = len(edges) # number of edges
    num_n = len(vertices) # number of vertices

    poses = []
    if len(sys.argv) >= 4: # read pos file if exists
        pos_filename = sys.argv[3]
    else: # pos file does not exist
        make_pos_list(edges)
        pos_filename = "pos_list_for_draw_subgraphs.txt"

    with open(pos_filename) as f:
        for line in f:
            ar = line.strip().split()
            poses.append((int(ar[0]), int(ar[1])))

    axmax = margin[0]
    aymax = margin[1]
    astr = ""
    offset = [margin[0], margin[1]]
    count = 0
    with open(sys.argv[2]) as f:
        # draw each subgraph
        for line in f:
            ar = line.strip().split()
            subedges = map(int, ar)
            for i in range(len(subedges)):
                if subedges[i] == 0:
                    subedges[i] = -1
            (st, xmax, ymax) = draw_graph(offset, edges, subedges, poses)
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

    print('<svg xmlns="http://www.w3.org/2000/svg" ', end="")
    print('width="{0}" height="{1}">'.format(axmax + margin[0], aymax + margin[1]))
    print(astr)
    print('</svg>')

if __name__ == '__main__':
    main()
