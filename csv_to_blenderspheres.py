import sys

def generate_blender_line(coordinates, blenderLayer):
    # Write a line to generate a sphere object in Blender.
    varLayer = ["False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False"]
    varLayer[blenderLayer] = "True"
    layerStr = ','.join(str(layer) for layer in varLayer)
    return "bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=0.5, view_align=False, enter_editmode=False, location=(" + coordinates + "), rotation=(0,0,0), layers=(" + layerStr + "))"

def write_blender_script(outputFile):
    #Iterates through list of xyz coordinates, then writes each line of Blender code to an output file
    #
    coordLayer = 0  			#designates the desired Blender layer to add sphere objects to. Layer 1 in Blender = coordLayer 0
    with open(outputFile, 'w') as out:
        for xyz in coordList:
            if xyz == ',,' or '':
                coordLayer +=1
            else:
                line = generate_blender_line(xyz, coordLayer)
                out.write(line + '\n')

def usage():
    str="This script generates a text file containing a series of blender inputs, given a .csv file containing xyz coordinates\
    \n\n\nThe script takes two files as input, an input file name and an output \
    file name. The input file is expected to be a .csv file, while the output file\
    is expected to be .txt file. To run the script issue the following command:\n\n\n\
    \tpython csv_to_blenderspheres.py <input_file> <output_file>\n\n\n\
    For additional information consult the ReadMe at http://www.github.com/BradhamLab/Blender\n\n\n"
    print(str)


args = sys.argv[1:]
if len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], str):
    if args[0].endswith('.csv') and args[1].endswith('.txt'):
        with open(args[0]) as f:
            content = f.readlines()
            for crudeList in content:
                coordList = crudeList.split('\r')
        write_blender_script(args[1])
    else:
        usage()
else:
    usage()

	    
	    