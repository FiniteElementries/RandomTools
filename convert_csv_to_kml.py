import csv

def convert_csv_to_kml_ployline(fname):
    #Input the file name.
    fn = fname.split('.')[0]
    ext = fname.split('.')[1]
    
    data = csv.reader(open(fname), delimiter = ',')
    
    #Skip the 1st header row.
    data.next()
    
    #Open the file to be written.
    with open( fn + '.kml', 'w') as f:
        print("Start processing " + fname)
        #Writing the kml file.
        f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
        f.write("<kml xmlns='http://earth.google.com/kml/2.1'>\n")
        f.write("<Document>\n")
        f.write("<name>" + fname + '.kml' +"</name>\n")

        f.write("<Placemark>\n")

        f.write("<styleUrl>#m_ylw-pushpin23</styleUrl>\n")

        f.write("<LineString>\n")
        f.write("<tessellate>1</tessellate>\n")
        f.write("<coordinates>\n")

        for row in data:
            f.write(str(row[1]) + "," + str(row[0]) + ",0 ")

        f.write("</coordinates>\n")
        f.write("</LineString>\n")
        f.write("</Placemark>\n")
                    
        f.write("</Document>\n")
        f.write("</kml>\n")
        f.close()
        print "File Created. "

if __name__=="__main__":
    convert_csv_to_kml_ployline('test.csv')
