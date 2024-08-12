import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.ticker as ticker

# Copied and modified from: https://www.kaggle.com/code/arwani/auto-encoder/notebook
def plot(record):
    cmap = colors.ListedColormap(
        ['#000000', '#0074D9','#FF4136','#2ECC40','#FFDC00',
         '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25'])

    norm = colors.Normalize(vmin=0, vmax=10)
    def remove_tail_zeros(key, data, mode = 'inp'):
        data = data.cpu().numpy()
        data = data.astype(int)
        ndata = []
        for i in range(len(data)):
            ndata.append(data[i] - 1 if data[i] > 0 else 0)
        data = np.array(ndata)
        dim = Dimension[key]['inp_dim' if mode == 'inp' else 'out_dim']
        return data[:dim[0] * dim[1]].reshape(dim[0], dim[1])
    
    num_rows = len(record)
    num_cols = len(record[0])
    fig, ax = plt.subplots(num_rows, num_cols, figsize=(15, 5))
    for x in range(num_rows):
        for y in range(num_cols):
            name = list(record[x].keys())[y]
            if num_rows > 1 and num_cols > 1:
                sub_plot = ax[x,y]
            elif num_rows > 1:
                sub_plot = ax[x]
            else:
                sub_plot = ax[y]
            sub_plot.imshow(record[x][name], cmap=cmap, norm=norm)
            sub_plot.set_title(name) if x==0 else None
            sub_plot.xaxis.set_major_locator(ticker.NullLocator())
            sub_plot.yaxis.set_major_locator(ticker.NullLocator())
    plt.show()