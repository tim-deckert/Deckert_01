# Deckert, Timothy
# 1000-637-406
# 2017-09-01
# Assignment_00_03

import numpy as np

class cl_world:
    def __init__(self, objects=[], canvases=[]):
        self.objects = objects
        self.canvases = canvases
        # self.display

    def add_canvas(self, canvas):
        self.canvases.append(canvas)
        canvas.world = self

    def create_graphic_objects(self, canvas, filename):
        file = open(filename, 'r')
        data = file.read()
        file.close()

        if self.objects:
             canvas.delete("all")
	
        rows = data.splitlines()

        vertices = []
        faces = []

        for row in rows:

            coords = row.split(" ")

            if coords[0] == "v":
                vertices.append(coords)
            if coords[0] == "f":
                faces.append(coords)
            if coords[0] == "w":
                window = coords
            if coords[0] == "s":
                viewport = coords

        viewport[1] = int(float(viewport[1]) * float(canvas.cget("width")))
        viewport[2] = int(float(viewport[2]) * float(canvas.cget("height")))
        viewport[3] = int(float(viewport[3]) * float(canvas.cget("width")))
        viewport[4] = int(float(viewport[4]) * float(canvas.cget("height")))

        self.objects.append(canvas.create_rectangle(viewport[1], viewport[2], viewport[3], viewport[4], outline="red", width=2))

        vpx = (viewport[3] - viewport[1]) / (float(window[3]) - float(window[1]))
        vpy = (viewport[4] - viewport[2]) / (float(window[4]) - float(window[2]))

        for vertex in vertices:
            vertex[1] = viewport[1] + int(vpx * (float(vertex[1]) - float(window[1])))
            vertex[2] = viewport[2] + int(vpy * (float(window[4]) - float(vertex[2])))

        points = []

        for face in faces:
            for fp in face:
                if fp.isdigit():
                    points.append(vertices[int(fp)-1][1])
                    points.append(vertices[int(fp)-1][2])
        
            self.objects.append(canvas.create_polygon(points, outline="red", fill="yellow"))
            points = []
        #print (vertices)
        #print (faces)
        #print (window)
        #print (viewport)
        #print (canvas.cget("width"))
        #print (canvas.cget("height"))

    def redisplay(self, canvas, event):
        if self.objects:
            for index, face in enumerate(self.objects):
                if index == 0:
                    
                print (canvas.coords(face))
            #canvas.coords(self.objects[0], 0, 0, event.width, event.height)
            #canvas.coords(self.objects[1], event.width, 0, 0, event.height)
            #canvas.coords(self.objects[2], int(0.25 * int(event.width)),
            #              int(0.25 * int(event.height)),
            #              int(0.75 * int(event.width)),
            #              int(0.75 * int(event.height)))
