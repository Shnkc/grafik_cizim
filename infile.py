'''
    Author : Sefa Koc
'''

from graph_tool.all import *
import  numpy
class InFile:
    def __init__(self, fname, outfname):
        self.f = open(fname, "r")
        self.ug  = Graph()
        self.ug.set_directed(False)
        self.outfname = outfname


    def decode(self):
        self.f.readline()
        numclusterline = self.f.readline()[:-1]
        splitted = numclusterline.split()

        #key: matrix'teki index
        #value: graph vertex

        self.pen_width = self.ug.new_edge_property("float")
        self.edge_color = self.ug.new_edge_property('float')
        self.users_vertices = {}
        self.keyw_vertices = {}
        self.issue_vertices = {}

        self.numCluster = int(splitted[len(splitted)-1])
        self.f.readline()
        for i in range(self.numCluster):
            for k in range(4):
                self.f.readline()
            clustersize = self.f.readline()[:-1]
            splitted = clustersize.split()
            sizes = splitted[1].split("x")
            sizes = map(int, sizes)
            for useri in range(sizes[0]):
                #user id oku
                user_line = self.f.readline()[:-1]
                splitted = user_line.split()
                user_id = int(splitted[len(splitted)-1])
                if user_id not in self.users_vertices:
                    self.users_vertices[user_id] = self.ug.add_vertex()

                #keywordlerin idlerini oku
                keyw_line = self.f.readline()[:-1]
                keyw_inds = keyw_line.split()
                keyw_map = {}
                keyw_i = 0
                for keyw_col in keyw_inds:
                    if keyw_col.startswith("S-"):
                        keyw_ind = int(keyw_col[2:])
                        keyw_map[keyw_i] = keyw_ind
                        if keyw_ind not in self.keyw_vertices:
                            self.keyw_vertices[keyw_ind] = self.ug.add_vertex()
                        keyw_i += 1

                #issue id ve hucreleri oku
                for rowid in range(sizes[2]):
                    row = self.f.readline()[:-1]
                    cells_in_row = row.split()
                    cell_index = 0
                    issue_ind = -1
                    while issue_ind < 0:
                        cell = cells_in_row[cell_index]
                        if cell.startswith("G-"):
                            issue_ind = int(cell[2:])
                            if issue_ind not in self.issue_vertices:
                                self.issue_vertices[issue_ind] = self.ug.add_vertex()
                            cell_index += 1

                    keyw_i = 0
                    while (cell_index + keyw_i) < len(cells_in_row):
                        cell = cells_in_row[cell_index+keyw_i]
                        if cell != ".":
                            edge = self.ug.add_edge(self.users_vertices[user_id], self.issue_vertices[issue_ind])
                            self.pen_width[edge] = 0.3
                            self.edge_color[edge] = 0.1
                            edge = self.ug.add_edge(self.users_vertices[user_id], self.keyw_vertices[keyw_map[keyw_i]])
                            self.pen_width[edge] = 0.3
                            self.edge_color[edge] = 0.4
                            edge = self.ug.add_edge(self.issue_vertices[issue_ind], self.keyw_vertices[keyw_map[keyw_i]])
                            self.pen_width[edge] = 0.3
                            self.edge_color[edge] = 0.7
                        keyw_i += 1


                self.f.readline()

    def draw_graph(self):
        total_node_count = 0
        fill_color = self.ug.new_vertex_property('int') #('vector<double>')
        shape = self.ug.new_vertex_property("string")
        size = self.ug.new_vertex_property("int")
        for vertex in self.users_vertices.values():
            total_node_count+=1
            fill_color[int(str(vertex))] = 1 #(1,0,0,0.9)
            shape[vertex] = "circle"
            size[vertex] = 7
        for vertex in self.issue_vertices.values():
            total_node_count+=1
            fill_color[int(str(vertex))] = 2 #(0,0,1,0.9)
            shape[vertex] = "square"
            size[vertex] = 15
        for vertex in self.keyw_vertices.values():
            total_node_count+=1
            fill_color[int(str(vertex))] = 3 #(0,1,0,0.9)
            shape[vertex] = "triangle"
            size[vertex] = 15

        text_pos = self.ug.new_vertex_property("int")
        color = self.ug.new_vertex_property("float")
        prop = self.ug.new_vertex_property("string")
        piece = 360.0 / total_node_count
        for i in range(total_node_count):
            prop[i] = "Degree %d" %i
            text_pos[i] = piece * i
            color[i] = 0
        state = minimize_nested_blockmodel_dl(self.ug, deg_corr=False)
        # state = minimize_blockmodel_dl(self.ug, deg_corr=True)
        # draw_hierarchy(state, output=self.outfname)
        state.draw(output=self.outfname,
                   vertex_fill_color=fill_color,
                   # vertex_text=prop,
                   # vertex_text_position="centered",
                   vertex_font_size=5,
                   vertex_size = size,
                   vertex_color = color,
                   vertex_shape = shape,
                   edge_pen_width=self.pen_width,
                   edge_color=self.edge_color)
        print(total_node_count)