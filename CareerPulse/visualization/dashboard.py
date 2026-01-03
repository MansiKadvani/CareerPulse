import matplotlib.pyplot as plt
import matplotlib.image as mpimg #used for reading img files

def dashboard() :

    #create figure with 2 rows and 3 columns 
    fig , ax = plt.subplots(2,3,figsize=(18,10))
    fig.suptitle("CareerPulse – Placement Intelligence Dashboard", color='brown', fontsize=18)

    #path of all images figures
    charts = [
        r'D:\Projects\CareerPulse\reports\multi_scatter_salary.png',
        r'D:\Projects\CareerPulse\reports\placement_score_histogram.png',
        r'D:\Projects\CareerPulse\reports\score_trend_line_plot.png',
        r'D:\Projects\CareerPulse\reports\top_students_bar.png',
        r'D:\Projects\CareerPulse\reports\weak_skill_pie.png'
    ]

    #making another list for positioning 
    pos = [(0,0),(0,1),(0,2),(1,0),(1,1)]

    '''
        zip() -> join/pairs two list side by side so we can loop through both at 
        same time
        For ex :- a = [1,2,3,4,5] & b = ['a','b','c','d','e']
            so output like 1 'a' , 2 'b' , 3 'c' , 4 'd' , 5 'e'
    '''

    #loop that place each image at right position
    for path , position in zip(charts,pos) :
        img = mpimg.imread(path) #read the image
        ax[position].imshow(img) #putting image in its subplot box
        ax[position].axis('off')
    
    ax[1,2].axis('off')
    plt.tight_layout()
    plt.savefig(r'D:\Projects\CareerPulse\reports\dashboard.png')
    plt.close()
