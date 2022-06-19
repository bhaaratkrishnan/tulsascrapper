from fileinput import filename


def create_pdf(content_list, dir):
    from fpdf import FPDF
    import nltk
    file_name=dir+"".join([i for i in content_list[0] if i.isalnum()])+".txt"
    content=content_list[1].split()
    file=open(file_name, "w", encoding="utf-8")
    for i in range(0,len(content),10):
        temp=" ".join(content[i:i+10])
        if "/" in temp:
            temp.replace("/"," ")
        file.write(temp)
        file.write("\n")
    file.close()
    print("File written")
