def extract_status200():
    filters = [
        "pdf",
        "jpg",
        "png",
        "jpeg",
        "xml"
    ]
    
    lines = open("C:/KrakenTools/KrakenInyection/Results/DeepFind_output.txt", "r").read().split("\n")
    check = False
    returnLines = []

    for line in lines:
        if line == "STATUS 200 OK":
            check = True
        elif line == "STATUS 404 NOT FOUND":
            check = False
        
        if check == True:
            # Filter
            if line[0] != "-":
                # Filter
                if line != "STATUS 200 OK":
                    checkFilter = True
                    
                    # Filter array, prevent URL to documents
                    for filter in filters:
                        if line.endswith(filter):
                            checkFilter = False
                        elif "#" in line:
                            checkFilter = False
                            
                    # Permission for add to returnLines
                    if checkFilter:
                        returnLines.append(line)
                
    return returnLines

def extract_URLRoot():
    lines = open("C:/KrakenTools/KrakenInyection/Results/DeepFind_output.txt", "r").read().split("\n")
    
    for line in lines:
        if "URL ROOT" in line:
            root = line.split("URL ROOT: ")
            
            return root[1]