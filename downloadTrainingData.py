import os, urllib.request, shutil, gzip

datapath = "../../training_data/MNISTData/"

def download():
    if not os.path.exists(datapath):
        os.makedirs(datapath)

    urls = ["http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz",
            "http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz",
            "http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz",
            "http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz"]
#lul
    for url in urls:
        filename = url.split("/")[-1]

        if os.path.exists(datapath+filename) or os.path.exists(datapath+os.path.splitext(filename)[0]):
            print(filename, ' already exists')
        else:
            print('Downloading ', filename)
            urllib.request.urlretrieve(url, datapath+filename)
    print('Download Complete')

def extract():
    files = os.listdir(datapath)
    for file in files:
        if file.endswith("gz"):
            print("Extracting ", file)
            with gzip.open(datapath+file, "rb") as f_in:
                with open(datapath+file.split('.')[0], "wb") as f_out:
                    shutil.copyfileobj(f_in, f_out)
    print("Extraction Complete")

    ##Remove archives
    for file in files:
        if file.endswith("gz"):
            print("Deleting archive ", file)
            os.remove(datapath+file)

download()
extract()
print("Files location "+datapath)