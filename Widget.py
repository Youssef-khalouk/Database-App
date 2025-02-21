from tkinter import *
import sqlite3
from tkfontawesome import icon_to_image 

# import ctypes

# # Enable high-DPI awareness
# try:
#     ctypes.windll.shcore.SetProcessDpiAwareness(1)
# except Exception as e:
#     print(f"Failed to set DPI awareness: {e}")

def rounded_points( x:int , y:int , width:int , height:int , r:int =0):
    corner_reduce=[[],[0],[1],[1],[2],[2,0],[2,1],[2,1,0],[2,2,0],[2,2,1],[3,2,1],[4,2,1],[4,2,1,0],
        [4,2,1,1],[4,2,2,1],[4,2,2,1,0],[4,2,2,1,1],[4,3,2,1,1],[5,3,2,1,1],[5,3,2,2,1],[5,3,2,2,1,0]]
    if r > width/2:
        r = int(width/2)
    if r > height/2:
        r = int(height/2)

    x2 = x + width
    y2 = y + height
    the_x = x
    the_y = y + r
    the_x1 = x2 - r
    the_y1 = y
    the_x2 = x2 
    the_y2 = y2 -r
    the_x3 = x + r
    the_y3 =y2  

    points = []
    anit_alising_points1 = []
    anit_alising_points2 = []

    top_left = [the_x,the_y]
    top_right = [the_x1,the_y1]
    bottom_right = [the_x2,the_y2]
    bottom_left = [the_x3,the_y3]

    aap_top_left1 = [the_x,the_y-1]
    aap_top_right1 = []
    aap_bottom_right1 = []
    aap_bottom_left1 = []

    aap_top_left2 = [the_x,the_y+1] 
    aap_top_right2 = [the_x1-1,the_y1]
    aap_bottom_right2 = [the_x2,the_y2-1]
    aap_bottom_left2 = [the_x3+1,the_y3]

    if r > 2:
        aap_top_left2.append(the_x+1) , aap_top_left2.append(the_y+1)
        aap_top_right2.append(the_x1-1) , aap_top_right2.append(the_y1+1)
        aap_bottom_right2.append(the_x2-1) , aap_bottom_right2.append(the_y2-1)
        aap_bottom_left2.append(the_x3+1) , aap_bottom_left2.append(the_y3-1)

    aap_top_left1.append( the_x )
    aap_bottom_right1.append( the_x2 )
    if r < 10 :
        aap_top_left1.append( the_y-1 )
        aap_top_right1.append( the_x1+1 )
        aap_bottom_right1.append( the_y2+1 )
        aap_bottom_left1.append( the_x3-1 ) 
    else:
        aap_top_left1.append( the_y-2 )
        aap_top_right1.append( the_x1+2 )
        aap_bottom_right1.append( the_y2+2 )
        aap_bottom_left1.append( the_x3-2 )
    aap_top_right1.append(the_y1)
    aap_bottom_left1.append( y2 )
    

    for row in corner_reduce[r]:
        if row != 0:
            the_x += 1
            top_left.append( the_x ),top_left.append( the_y - 1 )
            aap_top_left1.append( the_x ),aap_top_left1.append( the_y - 2 )
            aap_top_left2.append( the_x ),aap_top_left2.append( the_y )
            the_y -= row
            top_left.append( the_x ),top_left.append( the_y )
            aap_top_left1.append( the_x ),aap_top_left1.append( the_y-1 )
            aap_top_left2.append( the_x ),aap_top_left2.append( the_y+1 )

            the_y1 += 1
            top_right.append( the_x1 +1),top_right.append( the_y1 )
            aap_top_right1.append( the_x1+2 ),aap_top_right1.append( the_y1 )
            aap_top_right2.append( the_x1 ),aap_top_right2.append( the_y1 )
            the_x1 += row
            top_right.append( the_x1 ),top_right.append( the_y1 )
            aap_top_right1.append( the_x1+1 ),aap_top_right1.append( the_y1 )
            aap_top_right2.append( the_x1-1 ),aap_top_right2.append( the_y1 )

            the_x2 -= 1
            bottom_right.append( the_x2 ),bottom_right.append( the_y2+1 )
            aap_bottom_right1.append( the_x2 ),aap_bottom_right1.append( the_y2+2 )
            aap_bottom_right2.append( the_x2 ),aap_bottom_right2.append( the_y2 )
            the_y2 += row
            bottom_right.append( the_x2 ),bottom_right.append( the_y2 )
            aap_bottom_right1.append( the_x2 ),aap_bottom_right1.append( the_y2+1 )
            aap_bottom_right2.append( the_x2 ),aap_bottom_right2.append( the_y2-1 )

            the_y3 -= 1
            bottom_left.append( the_x3-1 ),bottom_left.append( the_y3 )
            aap_bottom_left1.append( the_x3-2 ),aap_bottom_left1.append( the_y3 )
            aap_bottom_left2.append( the_x3 ),aap_bottom_left2.append( the_y3 )
            the_x3 -= row
            bottom_left.append( the_x3 ),bottom_left.append( the_y3 )
            aap_bottom_left1.append( the_x3-1 ),aap_bottom_left1.append( the_y3 )
            aap_bottom_left2.append( the_x3+1 ),aap_bottom_left2.append( the_y3 )

        else:
            the_x += 1
            the_y -= 1
            top_left.append( the_x ),top_left.append( the_y )
            aap_top_left1.append( the_x ),aap_top_left1.append( the_y-1)
            aap_top_left2.append( the_x ),aap_top_left2.append( the_y+1)
            
            the_x1 += 1
            the_y1 += 1
            top_right.append( the_x1 ),top_right.append( the_y1 )
            aap_top_right1.append( the_x1),aap_top_right1.append( the_y1-1)
            aap_top_right2.append( the_x1 ),aap_top_right2.append( the_y1+1)

            the_x2 -= 1
            the_y2 += 1
            bottom_right.append( the_x2 ),bottom_right.append( the_y2 )
            aap_bottom_right1.append( the_x2 ),aap_bottom_right1.append( the_y2+1 )
            aap_bottom_right2.append( the_x2 ),aap_bottom_right2.append( the_y2-1 )

            the_x3 -= 1
            the_y3 -= 1
            bottom_left.append( the_x3 ),bottom_left.append( the_y3 )
            aap_bottom_left1.append( the_x3-1),aap_bottom_left1.append( the_y3 )
            aap_bottom_left2.append( the_x3 ),aap_bottom_left2.append( the_y3-1 )

    aa = corner_reduce[r].copy()
    aa.reverse()

    for row in aa:
        if row != 0:
            the_y -=1
            top_left.append(the_x+ 1),top_left.append(the_y)
            aap_top_left1.append( the_x ),aap_top_left1.append( the_y )
            aap_top_left2.append( the_x+2),aap_top_left2.append( the_y )
            the_x += row
            top_left.append(the_x),top_left.append(the_y)
            aap_top_left1.append( the_x-1 ),aap_top_left1.append( the_y)
            aap_top_left2.append( the_x+1),aap_top_left2.append( the_y)

            the_x1 +=1
            top_right.append(the_x1),top_right.append(the_y1+1)
            aap_top_right1.append( the_x1 ),aap_top_right1.append( the_y1)
            aap_top_right2.append( the_x1),aap_top_right2.append( the_y1+2)
            the_y1 += row
            top_right.append(the_x1),top_right.append(the_y1)
            aap_top_right1.append( the_x1),aap_top_right1.append( the_y1-1)
            aap_top_right2.append( the_x1),aap_top_right2.append( the_y1+1)

            the_y2 +=1
            bottom_right.append(the_x2-1),bottom_right.append(the_y2)
            aap_bottom_right1.append( the_x2 ),aap_bottom_right1.append( the_y2 )
            aap_bottom_right2.append( the_x2-2 ),aap_bottom_right2.append( the_y2 )
            the_x2 -= row
            bottom_right.append(the_x2),bottom_right.append(the_y2)
            aap_bottom_right1.append( the_x2+1 ),aap_bottom_right1.append( the_y2 )
            aap_bottom_right2.append( the_x2-1 ),aap_bottom_right2.append( the_y2 )

            the_x3 -=1
            bottom_left.append(the_x3),bottom_left.append(the_y3-1)
            aap_bottom_left1.append( the_x3 ),aap_bottom_left1.append( the_y3 )
            aap_bottom_left2.append( the_x3 ),aap_bottom_left2.append( the_y3-2 )
            the_y3 -= row
            bottom_left.append(the_x3),bottom_left.append(the_y3)
            aap_bottom_left1.append( the_x3 ),aap_bottom_left1.append( the_y3+1 )
            aap_bottom_left2.append( the_x3 ),aap_bottom_left2.append( the_y3-1 )

    aap_top_right1.append( x2)
    aap_bottom_left1.append( x )
    if r < 10 :
        aap_top_left1.append( x+r-1)
        aap_top_right1.append(y+r-1 )
        aap_bottom_right1.append( x2-r+1 )
        aap_bottom_left1.append( y2-r+1 )
    else:
        aap_top_left1.append( x+r-2)
        aap_top_right1.append(y+r-2)
        aap_bottom_right1.append( x2-r+2 )
        aap_bottom_left1.append( y2-r+2 )
    aap_top_left1.append( y )
    aap_bottom_right1.append( y2 )
    aap_bottom_left1.append( x ),aap_bottom_left1.append( y+r-1 )

    if r > 2 :
        aap_top_left2.append( x+r+1),aap_top_left2.append( y+1)
        aap_top_right2.append(x2-1),aap_top_right2.append(y+r+1)
        aap_bottom_right2.append( x2-r-1 ),aap_bottom_right2.append( y2-1 )
        aap_bottom_left2.append( x+1 ),aap_bottom_left2.append( y2-r-1 )
    aap_top_left2.append( x+r+1),aap_top_left2.append( y)
    aap_top_right2.append(x2),aap_top_right2.append(y+r+1)
    aap_bottom_right2.append( x2-r-1 ),aap_bottom_right2.append( y2 )
    aap_bottom_left2.append( x ),aap_bottom_left2.append( y2-r-1 )

    top_left.append(x+r),top_left.append(y)
    top_right.append(x2),top_right.append(y+r)
    bottom_right.append(x2 - r ),bottom_right.append(y2)
    bottom_left.append(x),bottom_left.append(y2-r)
    bottom_left.append(x),bottom_left.append(y + r)

    points.extend(top_left)
    points.extend(top_right)
    points.extend(bottom_right)
    points.extend(bottom_left)
    anit_alising_points1.extend(aap_top_left1)
    anit_alising_points1.extend(aap_top_right1)
    anit_alising_points1.extend(aap_bottom_right1)
    anit_alising_points1.extend(aap_bottom_left1)
    anit_alising_points2.extend(aap_top_left2)
    anit_alising_points2.extend(aap_top_right2)
    anit_alising_points2.extend(aap_bottom_right2)
    anit_alising_points2.extend(aap_bottom_left2)
    if r == 0 or r == 1:
        anit_alising_points1=[0,0,0,0]
        anit_alising_points2=[0,0,0,0]

    return points , anit_alising_points1 , anit_alising_points2

Colors_dectionery={'white':'#ffffff','black':'#000000','red':'#ff0000','blue':'#0000ff','green':'#00ff00',
    'yellow':'#ffff00','grey':'#7f7f7f','aliceblue': '#F0F8FF', 'antiquewhite': '#FAEBD7', 'antiquewhite1': '#FFEFDB', 
    'antiquewhite2':'#EEDFCC','antiquewhite3':'#CDC0B0','antiquewhite4':'#8B8378', 
    'aqua': '#00FFFF','aquamarine1': '#7FFFD4', 'aquamarine2': '#76EEC6', 'aquamarine3': '#66CDAA', 
    'aquamarine4':'#458B74', 'azure1': '#F0FFFF', 'azure2': '#E0EEEE', 'azure3': '#C1CDCD', 
    'azure4':'#838B8B', 'banana': '#E3CF57', 'beige': '#F5F5DC', 'bisque1': '#FFE4C4', 
    'bisque2':'#EED5B7', 'bisque3': '#CDB79E', 'bisque4': '#8B7D6B', 'black': '#000000',
    'blanchedalmond':'#FFEBCD', 'blue': '#0000FF', 'blue2': '#0000EE', 'blue3': '#0000CD',
    'blue4': '#00008B', 'blueviolet': '#8A2BE2', 'brick': '#9C661F', 'burntsienna': '#8A360F',
    'brown': '#A52A2A', 'brown1': '#FF4040', 'brown2': '#EE3B3B', 'brown3': '#CD3333', 
    'brown4': '#8B2323', 'burlywood': '#DEB887', 'burlywood1': '#FFD39B', 'burlywood2': '#EEC591', 
    'burlywood3': '#CDAA7D', 'burlywood4': '#8B7355', 'burntumber': '#8A3324', 'cadetblue': '#5F9EA0', 
    'cadetblue1': '#98F5FF', 'cadetblue2': '#8EE5EE', 'cadetblue3': '#7AC5CD', 'cadetblue4': '#53868B', 
    'cadmiumorange': '#FF6103', 'cadmiumyellow': '#FF9912', 'carrot': '#ED9121', 'chartreuse1': '#7FFF00', 
    'chartreuse2': '#76EE00', 'chartreuse3': '#66CD00', 'chartreuse4': '#458B00', 'chocolate': '#D2691E', 
    'chocolate1': '#FF7F24', 'chocolate2': '#EE7621', 'chocolate3': '#CD661D', 'chocolate4': '#8B4513', 
    'cobalt': '#3D59AB', 'cobaltgreen': '#3D9140', 'coldgrey': '#808A87', 'coral': '#FF7F50', 'coral1': '#FF7256', 
    'coral2': '#EE6A50', 'coral3': '#CD5B45', 'coral4': '#8B3E2F', 'cornflowerblue': '#6495ED', 
    'cornsilk1': '#FFF8DC', 'cornsilk2': '#EEE8CD', 'cornsilk3': '#CDC8B1', 'cornsilk4': '#8B8878', 
    'crimson': '#DC143C', 'cyan2': '#00EEEE', 'cyan3': '#00CDCD', 'cyan4': '#008B8B', 'darkgoldenrod': '#B8860B', 
    'darkgoldenrod1': '#FFB90F', 'darkgoldenrod2': '#EEAD0E', 'darkgoldenrod3': '#CD950C', 'darkgoldenrod4': '#8B6508', 
    'darkgray': '#A9A9A9', 'darkgreen': '#006400', 'darkkhaki': '#BDB76B', 'darkolivegreen': '#556B2F', 
    'darkolivegreen1': '#CAFF70', 'darkolivegreen2': '#BCEE68', 'darkolivegreen3': '#A2CD5A', 
    'darkolivegreen4': '#6E8B3D', 'darkorange': '#FF8C00', 'darkorange1': '#FF7F00', 'darkorange2': '#EE7600', 
    'darkorange3':'#CD6600','darkorange4': '#8B4500', 'darkorchid': '#9932CC', 'darkorchid1': '#BF3EFF', 
    'darkorchid2':'#B23AEE','darkorchid3': '#9A32CD', 'darkorchid4': '#68228B', 'darksalmon': '#E9967A', 
    'darkseagreen':'#8FBC8F','darkseagreen1': '#C1FFC1', 'darkseagreen2': '#B4EEB4', 'darkseagreen3': '#9BCD9B', 
    'darkseagreen4':'#698B69','darkslateblue': '#483D8B', 'darkslategray': '#2F4F4F', 'darkslategray1': '#97FFFF', 
    'darkslategray2':'#8DEEEE','darkslategray3': '#79CDCD', 'darkslategray4': '#528B8B', 'darkturquoise': '#00CED1', 
    'darkviolet': '#9400D3', 'deeppink1': '#FF1493', 'deeppink2': '#EE1289', 'deeppink3': '#CD1076', 'deeppink4': '#8B0A50', 
    'deepskyblue1': '#00BFFF', 'deepskyblue2': '#00B2EE', 'deepskyblue3': '#009ACD', 'deepskyblue4': '#00688B', 
    'dimgray': '#696969', 'dodgerblue1': '#1E90FF', 'dodgerblue2': '#1C86EE', 'dodgerblue3': '#1874CD', 
    'dodgerblue4': '#104E8B', 'eggshell': '#FCE6C9', 'emeraldgreen': '#00C957', 'firebrick': '#B22222', 
    'firebrick1': '#FF3030', 'firebrick2': '#EE2C2C', 'firebrick3': '#CD2626', 'firebrick4': '#8B1A1A', 
    'flesh': '#FF7D40', 'floralwhite': '#FFFAF0', 'forestgreen': '#228B22', 'gainsboro': '#DCDCDC', 
    'ghostwhite': '#F8F8FF', 'gold1': '#FFD700', 'gold2': '#EEC900', 'gold3': '#CDAD00', 'gold4': '#8B7500', 
    'goldenrod': '#DAA520', 'goldenrod1': '#FFC125', 'goldenrod2': '#EEB422', 'goldenrod3': '#CD9B1D', 
    'goldenrod4': '#8B6914', 'gray': '#808080', 'gray1': '#030303', 'gray10': '#1A1A1A', 'gray11': '#1C1C1C', 
    'gray12': '#1F1F1F', 'gray13': '#212121', 'gray14': '#242424', 'gray15': '#262626', 'gray16': '#292929', 
    'gray17': '#2B2B2B', 'gray18': '#2E2E2E', 'gray19': '#303030', 'gray2': '#050505', 'gray20': '#333333', 
    'gray21': '#363636', 'gray22': '#383838', 'gray23': '#3B3B3B', 'gray24': '#3D3D3D', 'gray25': '#404040', 
    'gray26': '#424242', 'gray27': '#454545', 'gray28': '#474747', 'gray29': '#4A4A4A', 'gray3': '#080808', 
    'gray30': '#4D4D4D', 'gray31': '#4F4F4F', 'gray32': '#525252', 'gray33': '#545454', 'gray34': '#575757', 
    'gray35': '#595959', 'gray36': '#5C5C5C', 'gray37': '#5E5E5E', 'gray38': '#616161', 'gray39': '#636363', 
    'gray4': '#0A0A0A', 'gray40': '#666666', 'gray42': '#6B6B6B', 'gray43': '#6E6E6E', 'gray44': '#707070', 
    'gray45': '#737373', 'gray46': '#757575', 'gray47': '#787878', 'gray48': '#7A7A7A', 'gray49': '#7D7D7D', 
    'gray5': '#0D0D0D', 'gray50': '#7F7F7F', 'gray51': '#828282', 'gray52': '#858585', 'gray53': '#878787', 
    'gray54': '#8A8A8A', 'gray55': '#8C8C8C', 'gray56': '#8F8F8F', 'gray57': '#919191', 'gray58': '#949494', 
    'gray59': '#969696', 'gray6': '#0F0F0F', 'gray60': '#999999', 'gray61': '#9C9C9C', 'gray62': '#9E9E9E', 
    'gray63': '#A1A1A1', 'gray64': '#A3A3A3', 'gray65': '#A6A6A6', 'gray66': '#A8A8A8', 'gray67': '#ABABAB', 
    'gray68': '#ADADAD', 'gray69': '#B0B0B0', 'gray7': '#121212', 'gray70': '#B3B3B3', 'gray71': '#B5B5B5', 
    'gray72': '#B8B8B8', 'gray73': '#BABABA', 'gray74': '#BDBDBD', 'gray75': '#BFBFBF', 'gray76': '#C2C2C2', 
    'gray77': '#C4C4C4', 'gray78': '#C7C7C7', 'gray79': '#C9C9C9', 'gray8': '#141414', 'gray80': '#CCCCCC', 
    'gray81': '#CFCFCF', 'gray82': '#D1D1D1', 'gray83': '#D4D4D4', 'gray84': '#D6D6D6', 'gray85': '#D9D9D9', 
    'gray86': '#DBDBDB', 'gray87': '#DEDEDE', 'gray88': '#E0E0E0', 'gray89': '#E3E3E3', 'gray9': '#171717', 
    'gray90': '#E5E5E5', 'gray91': '#E8E8E8', 'gray92': '#EBEBEB', 'gray93': '#EDEDED', 'gray94': '#F0F0F0', 
    'gray95': '#F2F2F2', 'gray97': '#F7F7F7', 'gray98': '#FAFAFA', 'gray99': '#FCFCFC', 'green': '#008000', 
    'green1': '#00FF00', 'green2': '#00EE00', 'green3': '#00CD00', 'green4': '#008B00', 'greenyellow': '#ADFF2F', 
    'honeydew1': '#F0FFF0', 'honeydew2': '#E0EEE0', 'honeydew3': '#C1CDC1', 'honeydew4': '#838B83', 
    'hotpink': '#FF69B4', 'hotpink1': '#FF6EB4', 'hotpink2': '#EE6AA7', 'hotpink3': '#CD6090', 'hotpink4': '#8B3A62', 
    'indianred': '#CD5C5C', 'indianred1': '#FF6A6A', 'indianred2': '#EE6363', 'indianred3': '#CD5555', 'indianred4': '#8B3A3A', 
    'indigo': '#4B0082', 'ivory1': '#FFFFF0', 'ivory2': '#EEEEE0', 'ivory3': '#CDCDC1', 'ivory4': '#8B8B83', 
    'ivoryblack': '#292421', 'khaki': '#F0E68C', 'khaki1': '#FFF68F', 'khaki2': '#EEE685', 'khaki3': '#CDC673', 
    'khaki4': '#8B864E', 'lavender': '#E6E6FA', 'lavenderblush1': '#FFF0F5', 'lavenderblush2': '#EEE0E5', 
    'lavenderblush3': '#CDC1C5', 'lavenderblush4': '#8B8386', 'lawngreen': '#7CFC00', 'lemonchiffon1': '#FFFACD', 
    'lemonchiffon2': '#EEE9BF', 'lemonchiffon3': '#CDC9A5', 'lemonchiffon4': '#8B8970', 'lightblue': '#ADD8E6', 
    'lightblue1': '#BFEFFF', 'lightblue2': '#B2DFEE', 'lightblue3': '#9AC0CD', 'lightblue4': '#68838B', 
    'lightcoral': '#F08080', 'lightcyan1': '#E0FFFF', 'lightcyan2': '#D1EEEE', 'lightcyan3': '#B4CDCD', 
    'lightcyan4': '#7A8B8B', 'lightgoldenrod1': '#FFEC8B', 'lightgoldenrod2': '#EEDC82', 'lightgoldenrod3': '#CDBE70', 
    'lightgoldenrod4': '#8B814C', 'lightgoldenrodyellow': '#FAFAD2', 'lightgrey': '#D3D3D3', 'lightpink': '#FFB6C1', 
    'lightpink1': '#FFAEB9', 'lightpink2': '#EEA2AD', 'lightpink3': '#CD8C95', 'lightpink4': '#8B5F65', 
    'lightsalmon1': '#FFA07A', 'lightsalmon2': '#EE9572', 'lightsalmon3': '#CD8162', 'lightsalmon4': '#8B5742', 
    'lightseagreen': '#20B2AA', 'lightskyblue': '#87CEFA', 'lightskyblue1': '#B0E2FF', 'lightskyblue2': '#A4D3EE', 
    'lightskyblue3': '#8DB6CD', 'lightskyblue4': '#607B8B', 'lightslateblue': '#8470FF', 'lightslategray': '#778899', 
    'lightsteelblue': '#B0C4DE', 'lightsteelblue1': '#CAE1FF', 'lightsteelblue2': '#BCD2EE', 'lightsteelblue3': '#A2B5CD', 
    'lightsteelblue4': '#6E7B8B', 'lightyellow1': '#FFFFE0', 'lightyellow2': '#EEEED1', 'lightyellow3': '#CDCDB4', 
    'lightyellow4': '#8B8B7A', 'limegreen': '#32CD32', 'linen': '#FAF0E6', 'magenta': '#FF00FF', 'magenta2': '#EE00EE', 
    'magenta3': '#CD00CD', 'magenta4': '#8B008B', 'manganeseblue': '#03A89E', 'maroon': '#800000', 'maroon1': '#FF34B3', 
    'maroon2': '#EE30A7', 'maroon3': '#CD2990', 'maroon4': '#8B1C62', 'mediumorchid': '#BA55D3', 'mediumorchid1': '#E066FF', 
    'mediumorchid2': '#D15FEE', 'mediumorchid3': '#B452CD', 'mediumorchid4': '#7A378B', 'mediumpurple': '#9370DB', 
    'mediumpurple1': '#AB82FF', 'mediumpurple2': '#9F79EE', 'mediumpurple3': '#8968CD', 'mediumpurple4': '#5D478B', 
    'mediumseagreen': '#3CB371', 'mediumslateblue': '#7B68EE', 'mediumspringgreen': '#00FA9A', 'mediumturquoise': '#48D1CC', 
    'mediumvioletred': '#C71585', 'melon': '#E3A869', 'midnightblue': '#191970', 'mint': '#BDFCC9', 'mintcream': '#F5FFFA', 
    'mistyrose1': '#FFE4E1', 'mistyrose2': '#EED5D2', 'mistyrose3': '#CDB7B5', 'mistyrose4': '#8B7D7B', 'moccasin': '#FFE4B5', 
    'navajowhite1': '#FFDEAD', 'navajowhite2': '#EECFA1', 'navajowhite3': '#CDB38B', 'navajowhite4': '#8B795E', 'navy': '#000080', 
    'oldlace': '#FDF5E6', 'olive': '#808000', 'olivedrab': '#6B8E23', 'olivedrab1': '#C0FF3E', 'olivedrab2': '#B3EE3A', 
    'olivedrab3': '#9ACD32', 'olivedrab4': '#698B22', 'orange': '#FF8000', 'orange1': '#FFA500', 'orange2': '#EE9A00', 
    'orange3': '#CD8500', 'orange4': '#8B5A00', 'orangered1': '#FF4500', 'orangered2': '#EE4000', 'orangered3': '#CD3700', 
    'orangered4': '#8B2500', 'orchid': '#DA70D6', 'orchid1': '#FF83FA', 'orchid2': '#EE7AE9', 'orchid3': '#CD69C9', 
    'orchid4': '#8B4789', 'palegoldenrod': '#EEE8AA', 'palegreen': '#98FB98', 'palegreen1': '#9AFF9A', 'palegreen2': '#90EE90', 
    'palegreen3': '#7CCD7C', 'palegreen4': '#548B54', 'paleturquoise1': '#BBFFFF', 'paleturquoise2': '#AEEEEE', 
    'paleturquoise3': '#96CDCD', 'paleturquoise4': '#668B8B', 'palevioletred': '#DB7093', 'palevioletred1': '#FF82AB', 
    'palevioletred2': '#EE799F', 'palevioletred3': '#CD6889', 'palevioletred4': '#8B475D', 'papayawhip': '#FFEFD5', 
    'peachpuff1': '#FFDAB9', 'peachpuff2': '#EECBAD', 'peachpuff3': '#CDAF95', 'peachpuff4': '#8B7765', 'peacock': '#33A1C9', 
    'pink': '#FFC0CB', 'pink1': '#FFB5C5', 'pink2': '#EEA9B8', 'pink3': '#CD919E', 'pink4': '#8B636C', 'plum': '#DDA0DD', 
    'plum1': '#FFBBFF', 'plum2': '#EEAEEE', 'plum3': '#CD96CD', 'plum4': '#8B668B', 'powderblue': '#B0E0E6', 'purple': '#800080', 
    'purple1': '#9B30FF', 'purple2': '#912CEE', 'purple3': '#7D26CD', 'purple4': '#551A8B', 'raspberry': '#872657', 
    'rawsienna': '#C76114', 'red1': '#FF0000', 'red2': '#EE0000', 'red3': '#CD0000', 'red4': '#8B0000', 'rosybrown': '#BC8F8F', 
    'rosybrown1': '#FFC1C1', 'rosybrown2': '#EEB4B4', 'rosybrown3': '#CD9B9B', 'rosybrown4': '#8B6969', 'royalblue': '#4169E1', 
    'royalblue1': '#4876FF', 'royalblue2': '#436EEE', 'royalblue3': '#3A5FCD', 'royalblue4': '#27408B', 'salmon': '#FA8072', 
    'salmon1': '#FF8C69', 'salmon2': '#EE8262', 'salmon3': '#CD7054', 'salmon4': '#8B4C39', 'sandybrown': '#F4A460', 'sapgreen': '#308014', 
    'seagreen1': '#54FF9F', 'seagreen2': '#4EEE94', 'seagreen3': '#43CD80', 'seagreen4': '#2E8B57', 'seashell1': '#FFF5EE', 
    'seashell2': '#EEE5DE', 'seashell3': '#CDC5BF', 'seashell4': '#8B8682', 'sepia': '#5E2612', 'sgibeet': '#8E388E', 
    'sgibrightgray': '#C5C1AA', 'sgichartreuse': '#71C671', 'sgidarkgray': '#555555', 'sgigray12': '#1E1E1E', 'sgigray16': '#282828', 
    'sgigray32': '#515151', 'sgigray36': '#5B5B5B', 'sgigray52': '#848484', 'sgigray56': '#8E8E8E', 'sgigray72': '#B7B7B7', 
    'sgigray76': '#C1C1C1', 'sgigray92': '#EAEAEA', 'sgigray96': '#F4F4F4', 'sgilightblue': '#7D9EC0', 'sgilightgray': '#AAAAAA', 
    'sgiolivedrab': '#8E8E38', 'sgisalmon': '#C67171', 'sgislateblue': '#7171C6', 'sgiteal': '#388E8E', 'sienna': '#A0522D', 
    'sienna1': '#FF8247', 'sienna2': '#EE7942', 'sienna3': '#CD6839', 'sienna4': '#8B4726', 'silver': '#C0C0C0', 'skyblue': '#87CEEB', 
    'skyblue1': '#87CEFF', 'skyblue2': '#7EC0EE', 'skyblue3': '#6CA6CD', 'skyblue4': '#4A708B', 'slateblue': '#6A5ACD', 
    'slateblue1': '#836FFF', 'slateblue2': '#7A67EE', 'slateblue3': '#6959CD', 'slateblue4': '#473C8B', 'slategray': '#708090', 
    'slategray1': '#C6E2FF', 'slategray2': '#B9D3EE', 'slategray3': '#9FB6CD', 'slategray4': '#6C7B8B', 'snow1': '#FFFAFA', 
    'snow2': '#EEE9E9', 'snow3': '#CDC9C9', 'snow4': '#8B8989', 'springgreen': '#00FF7F', 'springgreen1': '#00EE76', 
    'springgreen2': '#00CD66', 'springgreen3': '#008B45', 'steelblue': '#4682B4', 'steelblue1': '#63B8FF', 
    'steelblue2': '#5CACEE', 'steelblue3': '#4F94CD', 'steelblue4': '#36648B', 'tan': '#D2B48C', 'tan1': '#FFA54F', 
    'tan2': '#EE9A49', 'tan3': '#CD853F', 'tan4': '#8B5A2B', 'teal': '#008080', 'thistle': '#D8BFD8', 'thistle1': '#FFE1FF', 
    'thistle2': '#EED2EE', 'thistle3': '#CDB5CD', 'thistle4': '#8B7B8B', 'tomato1': '#FF6347', 'tomato2': '#EE5C42', 
    'tomato3': '#CD4F39', 'tomato4': '#8B3626', 'turquoise': '#40E0D0', 'turquoise1': '#00F5FF', 'turquoise2': '#00E5EE', 
    'turquoise3': '#00C5CD', 'turquoise4': '#00868B', 'turquoiseblue': '#00C78C', 'violet': '#EE82EE', 'violetred': '#D02090', 
    'violetred1': '#FF3E96', 'violetred2': '#EE3A8C', 'violetred3': '#CD3278', 'violetred4': '#8B2252', 'warmgrey': '#808069', 
    'wheat': '#F5DEB3', 'wheat1': '#FFE7BA', 'wheat2': '#EED8AE', 'wheat3': '#CDBA96', 'wheat4': '#8B7E66', 'white': '#FFFFFF', 
    'whitesmoke': '#F5F5F5', 'yellow1': '#FFFF00', 'yellow2': '#EEEE00', 'yellow3': '#CDCD00', 'yellow4': '#8B8B00'}

def mix_colors(color_1,color_2,c1_x=None,c2_x=None):
    if color_1[0] != '#' :
        color_1 = Colors_dectionery[color_1]
    if color_2[0] != '#':
        color_2 = Colors_dectionery[color_2]
    if not c1_x:
        if c2_x:
            c1_x = 1 - c2_x
        else:
            c1_x = 0.5
    if not c2_x:
        if c1_x:
            c2_x = 1-c1_x
        else:
            c2_x = 0.5
    x1 = int( int( color_1[1:3] ,16 ) * c1_x + int( color_2[1:3] ,16 ) *c2_x )
    x2 = int( int( color_1[3:5] ,16 ) * c1_x + int( color_2[3:5] ,16 ) *c2_x )
    x3 = int( int( color_1[5:7] ,16 ) * c1_x + int( color_2[5:7] ,16 ) *c2_x )
    return f'#{x1:02x}{x2:02x}{x3:02x}'

class Drow_angles :
    def __init__(self, master:any , bg:str ,bd:int =1 , outline:str =None , corner_reduce:int = 0 ):
        self.master = master
        self._bd :int = bd
        self._bg_drow = bg
        self._bd_color :str = outline
        self._outline :str = outline
        self._corner_reduce :int = corner_reduce
        self.anti_alising :float = 0.4
        if not self._bd_color :
            self._bd_color = bg
        self._outline_color :str = self._mix_colors(self._bd_color,master['bg'],c1_x=self.anti_alising)
        self._intline_color :str = self._mix_colors(self._bd_color,bg,c1_x=self.anti_alising)
        self.master.create_polygon(0,0,0,0,fill=bg,tag='polygon')
        self.master.create_line(0,0,0,0, fill=self._intline_color , width=self._bd,tag='inline')
        self.master.create_line(0,0,0,0, fill=self._outline_color , width=self._bd,tag='outline')
        self.master.create_line(0,0,0,0, fill=self._bd_color , width= self._bd,tag='line' )
    
    def _mix_colors(self,c1,c2,c1_x=None,c2_x=None):
        return mix_colors(c1,c2,c1_x=c1_x,c2_x=c2_x)

    def place(self,x,y,width,height):
        points , anit_alising_points1 , anit_alising_points2 =rounded_points(x+int(self._bd/2),
                                                                            y+int(self._bd/2),
                                                                            width-self._bd,
                                                                            height-self._bd,
                                                                            r=self._corner_reduce)
        self.master.coords('polygon',points)
        self.master.coords('outline',anit_alising_points1)
        self.master.coords('line',points)
        self.master.coords('inline',anit_alising_points2)
    
    def configure(self,outline :str= None,bg :str= None):
        if bg:
            if self._outline == None :
                self._bd_color = bg
                self.master.itemconfig('line',fill=bg)
                self.master.itemconfig('outline',fill=self._mix_colors(self._bd_color,self.master['bg'],c1_x=self.anti_alising))
            self._bg_drow=bg
            self.master.itemconfig('polygon',fill=bg)
            self.master.itemconfig('inline',fill=self._mix_colors(self._bd_color,bg,c1_x=self.anti_alising))
            self.master.itemconfig('outline',fill=self._mix_colors(self._bd_color,self.master['bg'],c1_x=self.anti_alising))
        if outline:
            if outline == 'update':
                self.master.itemconfig('line',fill=self._bd_color)
                self.master.itemconfig('outline',fill=self._mix_colors(self._bd_color,self.master['bg'],c1_x=self.anti_alising))
                self.master.itemconfig('inline',fill=self._mix_colors(self._bd_color,self._bg_drow,c1_x=self.anti_alising))
            else:
                self._bd_color = outline
                self.master.itemconfig('line',fill=outline)
                self.master.itemconfig('outline',fill=self._mix_colors(outline,self.master['bg'],c1_x=self.anti_alising))
                self.master.itemconfig('inline',fill=self._mix_colors(outline,self._bg_drow,c1_x=self.anti_alising))

    config = configure

class Round_Entry (Entry,Drow_angles) :
    def __init__(
                    self,
                    master: any,
                    text :str =None,
                    bg :str =None,
                    fg :str =None,
                    bd :int =1,
                    outline :str =None,
                    alpha :float =None,
                    outline_focus :str = None,
                    password : bool = False,
                    font = None ,
                    corner_reduce = 5,
                    **kwargs
                ):
        self._the_bg :str =bg
        self._bg :str = bg
        self._fg :str = fg
        self._text :str = text
        self._bd :int = bd
        self._outline :str = outline
        self._outline_focus :str = outline_focus
        self._master_bg :str =master['bg']
        self._fg_desible :str
        self._master = master
        self._master_olde_configure = master.configure
        self._alpha :float = alpha
        self._password :bool = password
        self._font = font
        self._corner_reduce :int = corner_reduce
        if not self._font:
            self._font = ('Candara',12,'normal')
        if not self._bg:
            self._bg='white'
            self._the_bg = 'white'
        if alpha :
            self._bg=self._mix_colors(self._bg,self._master_bg,c1_x=alpha)
        if alpha == 0:
            self._bg=self._master_bg

        self.canvas=Canvas(master=master,highlightthicknes=0,bg=self._master_bg)
        Entry.__init__( self , master=self.canvas ,relief='flat',fg=self._fg,font=self._font,bg=self._bg,**kwargs)
        Drow_angles.__init__(self,master=self.canvas,bg=self._bg,bd=self._bd,outline=self._outline,corner_reduce=corner_reduce)
        self.canvas.create_window((0,0),window=self,tag='entry')
        self.bind('<FocusIn>',self._focus_in)
        self.bind('<FocusOut>',self._focus_out)
        self._fg_desible = self._mix_colors(self._fg,self._bg,c1_x=0.3)
        if self._text:
            Entry.configure(self,fg=self._fg_desible)
            self.insert(0,self._text)
        self._bbox_entry()
        self._detect_master_bg()
        self.canvas.bind('<Configure>',lambda e: self._configure_itemes(self.canvas.winfo_width(),self.canvas.winfo_height()))
    
    def _bbox_entry(self):
        x0,y0,x1,y1=self.canvas.bbox('entry')
        self._set_sizes( (x1 - x0) +self._corner_reduce*2 +(self._bd*2) , (y1-y0) +2 +(self._bd*2))
        x0,y0,x1,y1=self.canvas.bbox('entry')
        self._set_sizes( (x1 - x0) +self._corner_reduce*2 +(self._bd*2) , (y1-y0) +2 +(self._bd*2))

    def _detect_master_bg(self):
        def my_config(**kwargs):
            self._master_olde_configure(**kwargs)
            if 'bg' in kwargs:
                self._master_bg=kwargs['bg']
                self.canvas.configure(bg=self._master_bg)
                if self._alpha != 1 :
                    if self._alpha != None:
                        self._bg = self._mix_colors(self._the_bg,self._master_bg,c1_x=self._alpha)
                        Drow_angles.configure(self,bg= self._bg )
                        Entry.configure(self,bg= self._bg )
                    else:
                        pass
                else:
                    self._bg = self._master_bg
                    Drow_angles.configure(self,bg= self._master_bg )
                    Entry.configure(self,bg= self._master_bg )
   
                self._fg_desible = self._mix_colors(self._fg,self._bg,c1_x=0.3)
                if self._text == Entry.get(self):
                    Entry.configure(self,fg=self._fg_desible)
        self._master.config = my_config
        self._master.configure = my_config

    def _configure_itemes(self,width,height):
        self.canvas.itemconfig('entry',width=width-self._corner_reduce*2-(self._bd*2))
        self.canvas.coords('entry', int(width/2),int(height/2) )
        Drow_angles.place(self,0,0,width,height)

    def _focus_in(self,event):
        if self._outline_focus :
                Drow_angles.configure(self,outline=self._outline_focus)
        if Entry.get(self) == self._text :
            Entry.configure(self,fg=self._fg)
            Entry.delete(self,0,'end')
        if self._password == True:
            Entry.configure(self,font=('Webdings',9,'normal'),show='=')

    def _focus_out(self,event):
        if self._outline_focus:
            if not self._outline:
                Drow_angles.configure(self,outline=self._bg)
            else:
                Drow_angles.configure(self,outline=self._outline)
        if self._text:
            if Entry.get(self) == '':
                Entry.configure(self,fg=self._fg_desible)
                Entry.insert(self,0,self._text)
        if self._password == True:
            if Entry.get(self) == self._text:
                if self._font:
                    Entry.configure(self,font=self._font,show='')
                else:
                    Entry.configure(self,font=('Candara',12,'normal'),show='')

    def _set_sizes(self,width,height):
        self._configure_itemes(width=width,height=height)
        self.canvas.configure(width=width,height=height)

    def _mix_colors(self,c1,c2,c1_x=None,c2_x=None):
        return mix_colors(c1,c2,c1_x=c1_x,c2_x=c2_x)

    def destroy(self):
        self._master.configure = self._master_olde_configure
        self._master.config = self._master_olde_configure
        Entry.destroy(self)
        self.canvas.destroy()

    def configure(self,**kwargs):
        if 'bg' in kwargs:
            self._bg =self._mix_colors(kwargs.pop('bg'),self._master_bg,c1_x=self._alpha)
            Drow_angles.configure(self,bg=self._bg)
            self._fg_desible = self._mix_colors(self._fg,self._bg,c1_x=0.3)
            Entry.configure(self,bg=self._bg)
            if self._text == Entry.get(self):
                Entry.configure(self,fg=self._fg_desible)
        if 'outline' in kwargs:
            self._outline = kwargs.pop('outline')
            Drow_angles.configure(self,outline=self._outline)
        if 'outline_focus'in kwargs:
            self._outline_focus = kwargs.pop('outline_focus')
        if 'font' in kwargs:
            Entry.configure(self,font=kwargs.pop('font'))
            self._bbox_entry()
        if 'fg' in kwargs:
            self._fg=kwargs.pop('fg')
            self._fg_desible = self._mix_colors(self._fg,self._bg,c1_x=0.3)
            if Entry.get(self) == self._text:
                Entry.configure(self,fg=self._fg_desible)
            else:
                Entry.configure(self,fg=self._fg)

    config = configure

    def winfo_width(self):
        return self.canvas.winfo_width()

    def winfo_height(self):
        return self.canvas.winfo_height()
    
    def get(self):
        if Entry.get(self) == self._text:
            return ''
        else:
            return Entry.get(self)

    def destroy(self):
        Entry.destroy(self)
        self.canvas.destroy()

    def pack(self,**kwargs):
        self.canvas.pack(**kwargs)

    def place(self,**kwargs):
        self.canvas.place(**kwargs)
    
    def grid(self,**kwargs):
        self.canvas.grid(**kwargs)

class Round_Button :
    def __init__(       
                    self,
                    master :any,
                    text :str =None,
                    fg :str ='black',
                    bd :int = 1,
                    compound :str ='left',
                    image =None,
                    command :any =None,
                    font :any =None,
                    width :int =None,
                    height :int =None,
                    bg :str = None,
                    bg_active :str =None,
                    outline :str =None,
                    anchor :str =None,
                    ipadx :int = 0,
                    ipady :int = 0,
                    alpha : float = None,
                    corner_reduce :int = 5,
                    **kwargs
                ):
        self._image :any =image
        self._bg :str
        self._command :any  =command
        self._compound : str = compound
        self._bg_active :str =bg_active 
        self._outline :str =outline
        self._bd :int =bd
        self._master :any= master
        self.master_olde_config :any =master.configure
        self._text :str = text
        self._w :int = width
        self._h :int = height
        self._width :int
        self._height :int
        self._ipadx : int =ipadx
        self._ipady : int = ipady
        self._alpha :float = alpha
        if bg == None:
            self._check_bg :bool = False
        else:
            self._check_bg :bool = True 
        if not bg:
            self._bg = master['bg']
        else:
            self._bg = bg
        if self._alpha != None:
            self._bg = self._mix_colors(self._bg,master['bg'],c1_x=self._alpha)

        self.canvas= Canvas(master=master,bg=master['bg'],highlightthicknes=0,**kwargs)   
        self.drow_angles=Drow_angles(master=self.canvas,bg=self._bg,bd=self._bd,outline=self._outline,corner_reduce=corner_reduce)
        self.canvas.create_text ((0,0),text=text,fill=fg,font=font,tags="text") 
        self.canvas.create_image ((0,0),image=image,tags="image")
        self._set_sizes()
        self._transparent()
        self.canvas.bind('<Enter>',self._enter)
        self.canvas.bind('<Leave>',self._leave)
        self.canvas.bind('<Button-1>',lambda event:self._leave(event,x=True))
        self.canvas.bind('<ButtonRelease-1>',self._click)
        self.canvas.bind('<Configure>',lambda e: self._drow_angles(self.canvas.winfo_width(),self.canvas.winfo_height()))
    

    def _drow_angles(self,width :int , height :int ):
        self.drow_angles.place(x=0,y=0,width=width,height=height)
        
    def _set_sizes(self):
        if self._image:
            x0, y0, x1, y1 = self.canvas.bbox("image")
            height1 = y1 - y0
            width1  = x1 - x0
        if self._text:
            x0, y0, x1, y1 = self.canvas.bbox("text")
            height2 = y1 - y0
            width2  = x1 - x0
        if self._compound == 'left':
            if self._text and self._image:
                self._width  = width1 + width2 +10 + self._ipadx*2
                self._height = max(height1 , height2)+4 + self._ipady*2
                if self._w:
                    self._width = self._w
                if self._h:
                    self._height = self._h
                image_x = width1/2 + 4 + self._ipady
                image_y = self._height/2
                text_x = self._width /2 + width1/2
                text_y = self._height/2      
        if self._compound == 'right':
            if self._text and self._image:
                self._width  = width1 + width2 +10 + self._ipadx*2
                self._height = max(height1 , height2)+4 + self._ipady*2
                if self._w:
                    self._width = self._w
                if self._h:
                    self._height = self._h
                image_x = self._width- width1/2 -4 - self._ipadx 
                image_y = self._height/2
                text_x = self._width/2 - 8
                text_y = self._height/2
        if self._compound == 'top':
            if self._text and self._image:
                self._width  = max(width1 , width2) + 4 + self._ipadx*2
                self._height = height1 + height2    +10 + self._ipady*2
                if self._w:
                    self._width = self._w
                if self._h:
                    self._height = self._h
                image_x = self._width/2 
                image_y = height1/2 + 2 + self._ipady
                text_x = self._width/2 
                text_y = self._height/2 + height1/2 +3
        if self._compound == 'bottom':
            if self._text and self._image:
                self._width  = max(width1 , width2) + 4 + self._ipadx*2
                self._height = height1 + height2    +10 + self._ipady*2
                if self._w:
                    self._width = self._w
                if self._h:
                    self._height = self._h
                image_x = self._width/2 
                image_y = self._height - height1/2 - 2 - self._ipady
                text_x = self._width/2 
                text_y = self._height/2 - height1/2 
        if self._image and not self._text :
            self._width = width1   +10 + self._ipadx
            self._height = height1 + 4 + self._ipady
            if self._w:
                self._width = self._w
            if self._h:
                self._height = self._h
            image_x = self._width /2
            image_y = self._height/2
        if self._text and not self._image:
            self._width = width2  +10 + self._ipadx
            self._height = height2+ 4 + self._ipady
            if self._w:
                self._width = self._w
            if self._h:
                self._height = self._h
            text_x = self._width /2
            text_y = self._height/2
        if self._image:
            self.canvas.coords('image' , image_x , image_y )  
        if self._text:
            self.canvas.coords('text' , text_x , text_y )
        self.canvas.configure( width=self._width , height=self._height )

    def _transparent(self):
        def _config(**kwargs):
            if 'bg' in kwargs:
                self.canvas.configure(bg=kwargs['bg'])
                if self._check_bg== True:
                    self.drow_angles.configure(bg=self._mix_colors(self._bg,kwargs['bg'],c1_x=self._alpha))
                else:
                    self._bg = kwargs['bg']
                    self.drow_angles.configure(bg=self._bg)
            self.master_olde_config(**kwargs)
        self._master.config=_config
        self._master.configure=_config

    def _enter(self,event):
        if self._bg_active:
            if self._alpha != None:
                self.drow_angles.configure(bg=self._mix_colors(self._bg_active,self._master['bg'],c1_x=self._alpha))
            else:
                self.drow_angles.configure(bg=self._bg_active)
        else:
            self.drow_angles.configure(bg=self._bg)

    def _leave(self,event,x :bool =False):
        if self._bg_active:
            if self._alpha != None:
                self.drow_angles.configure(bg=self._mix_colors(self._bg,self._master['bg'],c1_x=self._alpha))
            else:
                self.drow_angles.configure(bg=self._bg)
        elif x == True:
            self.drow_angles.configure(bg=self._mix_colors('black',self._master['bg'],c1_x=0.5))

    def _click(self,event):
        self._enter(event)
        if self._command:
            self._command()

    def destroy(self):
        self._master.config=self.master_olde_config
        self._master.configure=self.master_olde_config
        self.canvas.destroy()

    def _mix_colors(self,c1,c2,c1_x=None,c2_x=None):
        return mix_colors(c1,c2,c1_x=c1_x,c2_x=c2_x)

    def configure(self,**kwargs):
        if 'alpha' in kwargs:
            self._alpha = kwargs.pop('alpha')
            self.drow_angles.configure(bg=self._mix_colors(self._bg,self._master['bg'],c1_x=self._alpha))
        if 'bg' in kwargs:
            self._bg=kwargs.pop('bg')
            self.drow_angles.configure(bg=self._mix_colors(self._bg,self._master['bg'],c1_x=self._alpha))
        if 'outline' in kwargs:
            self._outline=kwargs.pop('outline')
            self.drow_angles.configure(outline=self._outline)
        if 'bg_active' in kwargs:
            self._bg_active=kwargs.pop('bg_active')
        if 'fg' in kwargs:
            self.canvas.itemconfig('text',fill=kwargs.pop('fg'))
        if 'bd' in kwargs: # not working yet
            self._bd=kwargs.pop('bd')
            self.drow_angles.configure(bd=self._bd)
        if 'image' in kwargs:
            self._image=kwargs.pop('image')
            self.canvas.itemconfig('image',image=self._image)
            self._set_sizes()
        if 'text' in kwargs:
            self._text=kwargs.pop('text')
            self.canvas.itemconfig('text',text=self._text)
            self._set_sizes()
        if 'font' in kwargs:
            self.canvas.itemconfig('text',font=kwargs.pop('font'))
            self._set_sizes()
        if 'compound' in kwargs:
            self._compound = kwargs.pop('compound')
            self._set_sizes()
        if 'command' in kwargs:
            self._command=kwargs.pop('command')
    
    config=configure

    def winfo_width(self):
        return self.canvas.winfo_width()

    def winfo_height(self):
        return self.canvas.winfo_height()

    def pack(self,**kwargs):
        self.canvas.pack(**kwargs)

    def place(self,**kwargs):
        self.canvas.place(**kwargs)

    def grid(self,**kwargs):
        self.canvas.grid(**kwargs)

class Scroll(Canvas):
    def __init__(
                        self, 
                        master :any,
                        width :int =None,
                        height :int =None,
                        bg :str =None ,
                        button_bg :str =None,
                        button_bg_active :str =None,
                        orient :str =None,
                        unit :int =None,
                        scroll_wheel :bool =False,
                        **kwargs
                ):
        self._bg :str 
        self._button_bg :str ='grey62'
        self._button_bg_active :str ='grey12'
        self._check :bool = True
        self._num :int
        self._y_or_x :int
        self._command :any = None
        self._set_color :bool = True
        self._h_or_w :int = 30
        self._p_y :int = 0
        self._p_x :int = 5
        self._count_to_close :int =0
        self._canvas_width :int =11
        self._canvas_height :int =11
        self._orient :str ='vertical'
        self._current_h_or_w : int
        self._teck_smaling :bool =True
        self._loset_point :  bool
        self._unit :int = 30
        self._x_and_y_set_ :list
        self._master :any =master

        if width:
            self._canvas_width=width
        if height:
            self._canvas_height=height
        if bg:
            self._bg=bg
        else:
            try:
                self._bg = master.cget('bg')
            except:
                self._bg ='white'
        if button_bg :
            self._button_bg=button_bg
        if button_bg_active:
            self._button_bg_active=button_bg_active
        if unit:
            self._unit=unit
        if orient:
            self._orient=orient
            if self._orient.lower()=='horizontal':
                self._p_y=6
                self._p_x=0
            else:
                if scroll_wheel:
                    self._secroll_wheel(master)
        else:
            if scroll_wheel:
                self._secroll_wheel(master)
        self._transparent()
        self.canvas=Canvas(master,highlightthicknes=0,
                                    width=self._canvas_width,
                                    height=self._canvas_height,
                                    bg=self._bg,
                                    **kwargs)
        self.polygon=self.canvas.create_polygon(self._points(0,0,0,0),fill=self._button_bg)
        self.canvas.tag_bind(self.polygon,'<B1-Motion>',self._move_button)
        self.canvas.tag_bind(self.polygon,'<ButtonRelease-1>',lambda e:self._set_true())
        self.canvas.tag_bind(self.polygon,'<Enter>',lambda e:self._up_button())
        self.canvas.tag_bind(self.polygon,'<Leave>',lambda e:self._down_button())
        
    def _secroll_wheel(self,master :any):
        def ent(event):
            self.canvas.bind_all('<MouseWheel>',self._mouse_scroll_event)
        def lev(event):
            self.canvas.bind_all('<MouseWheel>','')
        master.bind('<Enter>',ent)
        master.bind('<Leave>',lev)

    def _transparent(self):
        self.master_olde_configure=self._master.configure
        def _configure(**kwargs):
            if 'bg' in kwargs:
                self.canvas.configure(bg=kwargs['bg'])
            self.master_olde_configure(**kwargs)
        self._master.configure = _configure
        self._master.config = _configure
    
    def _up_button(self):
        self._count_to_close+=1
        self.canvas.itemconfig(self.polygon,fill=self._button_bg_active)
        def up_v():
            if self._p_x >=2:
                self._p_x-=1
                self.canvas.coords(self.polygon,self._points(self._p_x,self._p_y+1,10,self._current_h_or_w))
                self.canvas.after(30,up_v)
        def up_h():
            if self._p_y >=3:
                self._p_y-=1
                self.canvas.coords(self.polygon,self._points(self._p_x,self._p_y,self._current_h_or_w,10))
                self.canvas.after(30,up_h)
        if self._orient.lower()=='vertical':
            self.canvas.after(50,up_v)
        else:
            self.canvas.after(50,up_h)
    
    def _down_button(self):
        self._count_to_close+=1
        _check_var_=self._count_to_close
        if self._set_color is True:
            self.canvas.itemconfig(self.polygon,fill=self._button_bg)
        def down_v():
            if self._teck_smaling:
                if self._count_to_close == _check_var_ and self._set_color is True:
                    self._p_x+=1
                    self.canvas.coords(self.polygon,self._points(self._p_x,self._p_y+1,10,self._current_h_or_w))
                if self._p_x <5:
                    self.canvas.after(40,down_v)
        def down_h():
            if self._teck_smaling:
                if self._count_to_close == _check_var_ and self._set_color is True:
                    self._p_y+=1
                    self.canvas.coords(self.polygon,self._points(self._p_x,self._p_y,self._current_h_or_w,10))
                if self._p_y <6:
                    self.canvas.after(40,down_h)

        if self._orient.lower()=='vertical':    
            self.canvas.after(2000,down_v)
        else:
            self.canvas.after(2000,down_h)
    
    def _set_true(self):
        self._check=True
        self._set_color=True

    def _points(self, x:int , y:int , width:int , height:int ):
        if self._orient.lower() == 'vertical':
            w= width
            z= y + height
        else:
            w= x + width
            z= height   
        points=[x,y     , x+1,y   , x+1,y-1 ,
                w-1,y-1 , w-1,y   , w,y     ,
                w,z-1   , w-1,z-1 , w-1,z   ,
                x+1,z   , x+1,z-1 , x,z-1   ,]
        return points
    
    def _move_button(self,event):
        if self._check:
            self._set_color = False
            self.canvas.focus()
            if self._orient.lower()=='vertical':
                self._num=event.y_root
                self._y_or_x=self.canvas.coords(self.polygon)[1]+1
                self._loset_point=1-(self._current_h_or_w-1/self.canvas.winfo_height()-(self._current_h_or_w-1))
            else:
                self._num=event.x_root
                self._y_or_x=self.canvas.coords(self.polygon)[2]+1
                self._loset_point=1-(self._current_h_or_w-1/self.canvas.winfo_width()-(self._current_h_or_w-1))
            self._check=False   
        else:
            if self._command is not None:
                if self._orient.lower()=='vertical':
                    y=self._y_or_x+event.y_root-self._num
                    n_y=y/(self.canvas.winfo_height())
                    if n_y <= self._loset_point and n_y>= 0 :
                        self.set(n_y,0.0)
                else:
                    y=self._y_or_x+event.x_root-self._num
                    n_y=y/(self.canvas.winfo_width())
                    if n_y <= self._loset_point and n_y>= 0 :
                        self.set(n_y,0.0)
                self._command('moveto',n_y)
    
    def _mouse_scroll_event(self,event):
        if self._command and self._teck_smaling :
            h=self._x_and_y_set_[1]-self._x_and_y_set_[0]
            m_y=self._x_and_y_set_[0]
            if self._orient == 'vertical':
                if int(event.delta)==120:
                    m_y-= h/(self.canvas.winfo_height()/self._unit)
                else:
                    m_y+= h/(self.canvas.winfo_height()/self._unit)
            else:
                if int(event.delta)==120:
                    m_y-= h/(self.canvas.winfo_width()/self._unit)
                else:
                    m_y+= h/(self.canvas.winfo_width()/self._unit)
            self._command('moveto',m_y)
            # self._command('scroll', -int(event.delta/70), 'units')
    
    def set(self, _x: float, _y: float):
        self._x_and_y_set_=[float(_x),float(_y)]
        if self._orient.lower()=='vertical':
            f_h_or_w=self.canvas.winfo_height()-2
        else:
            f_h_or_w=self.canvas.winfo_width()-2
        if self._set_color:
            self._current_h_or_w = f_h_or_w * (float(_y)-float(_x))
            self._h_or_w=self._current_h_or_w
        if self._h_or_w < 30 :
            f_h_or_w=f_h_or_w-(30-self._h_or_w)
            self._current_h_or_w=30
        if self._current_h_or_w != f_h_or_w:
            if self._orient.lower()=='vertical':
                self._p_y=int( (f_h_or_w) * float(_x) )
                self.canvas.coords(self.polygon,self._points(self._p_x,self._p_y,10,self._current_h_or_w))
                self.canvas.moveto(self.polygon,x=self._p_x-1,y= self._p_y)
            else:
                self._p_x=int( (f_h_or_w) * float(_x) )
                self.canvas.coords(self.polygon,self._points(self._p_x,self._p_y,self._current_h_or_w,10))
                self.canvas.moveto(self.polygon,x=self._p_x-1,y= self._p_y-2)
            self._teck_smaling=True
        else:
            self._teck_smaling=False
            self.canvas.coords(self.polygon,self._points(0,0,0,0))
    
    def pack(self,**kwargs):
        self.canvas.pack(**kwargs)

    def place(self,**kwargs):
        self.canvas.place(**kwargs)

    def grid(self,**kwargs):
        self.canvas.grid(**kwargs)

    def destroy(self):
        self._master.configure=self.master_olde_configure
        self._master.config=self.master_olde_configure
        self.canvas.destroy()
    
    def configure(self,command=None,bg=None,button_bg=None,button_bg_active=None,**kwargs):
        if command:
            self._command=command
        if bg:
            self.canvas.configure(bg=bg)
            self._bg=bg
        if button_bg:
            self.canvas.itemconfig(self.polygon,fill=button_bg)
            self._button_bg=button_bg
        if button_bg_active:
            self._button_bg_active=button_bg_active
        self.canvas.configure(**kwargs)
    config=configure

class Scrolled_Frame(Frame):
    def __init__(
                    self,
                    master :any,
                    bg :str =None,
                    scroll_button_bg :str =None,
                    scroll_button_active :str =None,
                    scroll_unit :int =None,
                    scroll_vertical :bool =False,
                    scroll_horizontal :bool =False,
                    width :int =None,
                    height :int =None,
                    **kwargs
                ):
        self.frame=Frame(master,bg=bg,width=width,height=height,**kwargs)
        self.canvas=Canvas( self.frame,highlightthicknes=0,bg=bg,width=width,height=height)
        if scroll_vertical:
            self.scroll_v=Scroll(self.frame,
                                    bg=bg,
                                    button_bg=scroll_button_bg,
                                    button_bg_active=scroll_button_active,
                                    unit=scroll_unit,
                                    scroll_wheel=True)
            self.canvas.config(yscrollcommand=self.scroll_v.set)
            self.scroll_v.config(command=self.canvas.yview)
            self.scroll_v.pack(side='right',fill='y')
        if scroll_horizontal:
            self.scroll_h=Scroll(self.frame ,
                                    orient='horizontal',
                                    bg=bg,
                                    button_bg=scroll_button_bg,
                                    button_bg_active=scroll_button_active,
                                    unit=scroll_unit)
            self.canvas.config(xscrollcommand=self.scroll_h.set)
            self.scroll_h.config(command=self.canvas.xview)
            self.scroll_h.pack(side='bottom',fill='x')
        self.canvas.pack(side='left',fill='both',expand=1)
        Frame.__init__(self,master=self.canvas,bg=bg)
        self.bind('<Configure>',lambda e:self.canvas.configure(scrollregion=self.canvas.bbox('all')))
        self.window=self.canvas.create_window((0,0),window=self,anchor='nw')
        self.canvas.bind('<Configure>',lambda e:self._set_config(scroll_vertical,scroll_horizontal))
        
    def _set_config(self,vertical,horizontal):
        if vertical==False:
            self.canvas.itemconfig(self.window,height=self.canvas.winfo_height())
        if horizontal==False:
            self.canvas.itemconfig(self.window,width=self.canvas.winfo_width())
    
    def destroy(self):
        Frame.destroy(self)
        self.canvas.destroy()
        self.frame.destroy()

    def winfo_children(self):
        self.canvas.after(100,lambda:self.canvas.yview('moveto',0))
        return Frame.winfo_children(self)

    def configure(self,bg=None,scroll_button_bg=None,scroll_button_active=None,height=None,width=None,**kwargs):
        self.frame.configure(**kwargs)
        self.canvas.configure(bg=bg)
        Frame.configure(self,bg=bg)
        if height:
            Frame.config(self,height=height)
        if width:
            Frame.config(self,width=width)
        try:
            self.scroll_v.configure(bg=bg,button_bg=scroll_button_bg,button_bg_active=scroll_button_active)
        except:pass
        try:
            self.scroll_h.configure(bg=bg,button_bg=scroll_button_bg,button_bg_active=scroll_button_active)
        except:pass
    config=configure

    def pack(self,**kwargs):
        self.frame.pack(**kwargs)
    def place(self,**kwargs):
        self.frame.place(**kwargs)
    def grid(self,**kwargs):
        self.frame.grid(**kwargs)   

class Round_EntryBox (Entry,Drow_angles) :
    def __init__(
                    self,
                    master: any,
                    text :str =None,
                    bg :str =None,
                    fg :str =None,
                    bd :int =1,
                    outline :str =None,
                    alpha :float =None,
                    outline_focus :str = None,
                    password : bool = False,
                    font = None ,
                    corner_reduce = 5,
                    values = None,
                    **kwargs
                ):
        self._the_bg :str =bg
        self._bg :str = bg
        self._fg :str = fg
        self._text :str = text
        self._bd :int = bd
        self._outline :str = outline
        self._outline_focus :str = outline_focus
        self._master_bg :str =master['bg']
        self._fg_desible :str
        self._master = master
        self._master_olde_configure = master.configure
        self._alpha :float = alpha
        self._password :bool = password
        self._font = font
        self._corner_reduce :int = corner_reduce
        if not self._font:
            self._font = ('Candara',12,'normal')
        if not self._bg:
            self._bg='white'
            self._the_bg = 'white'
        if alpha :
            self._bg=self._mix_colors(self._bg,self._master_bg,c1_x=alpha)
        if alpha == 0:
            self._bg=self._master_bg
        self._f_click :bool = False
        self._values = values
        
        self.flash_image_u = icon_to_image('chevron-up',fill=self._outline,scale_to_width =14)
        self.flash_image_d = icon_to_image('chevron-down',fill=self._outline,scale_to_width =14)
        self.flash_image_u_enter = icon_to_image('chevron-up',fill=self._outline_focus,scale_to_width =14)
        self.flash_image_d_enter = icon_to_image('chevron-down',fill=self._outline_focus,scale_to_width =14)

        self.canvas=Canvas(master=master,highlightthicknes=0,bg=self._master_bg)
        Entry.__init__( self , master=self.canvas ,relief='flat',fg=self._fg,font=self._font,bg=self._bg,**kwargs)
        Drow_angles.__init__(self,master=self.canvas,bg=self._bg,bd=self._bd,outline=self._outline,corner_reduce=corner_reduce)
        self.canvas.create_window((0,0),window=self,tag='entry')
        self.canvas.create_image(0,0,image=self.flash_image_d,tag='f_image')
        self.bind('<FocusIn>',self._focus_in)
        self.bind('<FocusOut>',self._focus_out)
        self._fg_desible = self._mix_colors(self._fg,self._bg,c1_x=0.3)
        if self._text:
            Entry.configure(self,fg=self._fg_desible)
            self.insert(0,self._text)
        self._bbox_entry()
        self._detect_master_bg()
        self.canvas.tag_bind('f_image','<Enter>',self._flash_enter)
        self.canvas.tag_bind('f_image','<Leave>',self._flash_Leave)
        self.canvas.tag_bind('f_image','<Button-1>',self._flash_click)
        self.canvas.bind('<Configure>',lambda e: self._configure_itemes(self.canvas.winfo_width(),self.canvas.winfo_height()))
    
    def _bbox_entry(self):
        x0,y0,x1,y1=self.canvas.bbox('entry')
        self._set_sizes( (x1 - x0) +self._corner_reduce*2 +(self._bd*2) , (y1-y0) +2 +(self._bd*2))
        x0,y0,x1,y1=self.canvas.bbox('entry')
        self._set_sizes( (x1 - x0) +self._corner_reduce*2 +(self._bd*2) , (y1-y0) +2 +(self._bd*2))

    def _detect_master_bg(self):
        def my_config(**kwargs):
            self._master_olde_configure(**kwargs)
            if 'bg' in kwargs:
                self._master_bg=kwargs['bg']
                self.canvas.configure(bg=self._master_bg)
                if self._alpha != 1 :
                    if self._alpha != None:
                        self._bg = self._mix_colors(self._the_bg,self._master_bg,c1_x=self._alpha)
                        Drow_angles.configure(self,bg= self._bg )
                        Entry.configure(self,bg= self._bg )
                    else:
                        pass
                else:
                    self._bg = self._master_bg
                    Drow_angles.configure(self,bg= self._master_bg )
                    Entry.configure(self,bg= self._master_bg )
   
                self._fg_desible = self._mix_colors(self._fg,self._bg,c1_x=0.3)
                if self._text == Entry.get(self):
                    Entry.configure(self,fg=self._fg_desible)
        self._master.config = my_config
        self._master.configure = my_config

    def _configure_itemes(self,width,height):
        self.canvas.itemconfig('entry',width=width-(self._bd*2)-35)
        self.canvas.coords('entry', int(width/2)-5,int(height/2) )
        self.canvas.coords('f_image', width-13,int(height/2) )
        Drow_angles.place(self,0,0,width,height)

    def _focus_in(self,event):
        if self._outline_focus :
                Drow_angles.configure(self,outline=self._outline_focus)
        if Entry.get(self) == self._text :
            Entry.configure(self,fg=self._fg)
            Entry.delete(self,0,'end')
        if self._password == True:
            Entry.configure(self,font=('Webdings',9,'normal'),show='=')

    def _focus_out(self,event):
        if self._outline_focus:
            if not self._outline:
                Drow_angles.configure(self,outline=self._bg)
            else:
                Drow_angles.configure(self,outline=self._outline)
        if self._text:
            if Entry.get(self) == '':
                Entry.configure(self,fg=self._fg_desible)
                Entry.insert(self,0,self._text)
        if self._password == True:
            if Entry.get(self) == self._text:
                if self._font:
                    Entry.configure(self,font=self._font,show='')
                else:
                    Entry.configure(self,font=('Candara',12,'normal'),show='')

    def _showbox(self):
        width = self.canvas.winfo_width()
        self.can = Canvas(master=self._master,highlightthicknes=0,bg=self._master_bg)
        self.can.place( x=self.canvas.winfo_x(),
                        y=self.canvas.winfo_y()+3+self.canvas.winfo_height(),
                        width=width,height=98)
        drow=Drow_angles(master=self.can,bg=self._bg,bd=self._bd,outline=self._outline,corner_reduce=5)
        drow.place(x=0,y=0,width=width,height=98)
        frame = Frame(master=self.can,bg=self._bg)
        self.can.create_window(1,7,window=frame,tag='frame',anchor='nw')
        self.can.itemconfig('frame',width=width-2,height=84)
        scroll=Scroll(  frame,
                        bg=self._bg,
                        button_bg=self._outline,
                        button_bg_active=self._outline_focus,
                        unit=21,
                        scroll_wheel=True)
        scroll.pack(side='right',fill='y')
        self.can1= Canvas(frame,highlightthicknes=0,bg=self._bg)
        self.can1.bind('<Configure>',lambda e:self.can1.configure(scrollregion=self.can1.bbox('all')))
        self.can1.pack(side='left',fill='both',expand=True)
        self.can1.config(yscrollcommand=scroll.set)
        scroll.configure(command=self.can1.yview)
        fr=Frame(self.can1,bg='blue')
        self.can1.create_window((0,0),window=fr,anchor='nw',tag='fr1')
        self.can1.itemconfig('fr1',width=width)
        frame.focus()
        frame.bind('<FocusOut>',self._close_showbox)
        def button(row):
            var=Label(fr,text=row,bg=self._bg,fg=self._fg,justify='center')
            var.pack(fill='x')
            def enter(event):
                var.config(bg=mix_colors(self._bg,'black',.9))
            def leave(event):
                var.config(bg=self._bg)
            def click_chose(event):
                Entry.configure(self,fg=self._fg)
                self.focus()
                self.delete(0,END)
                self.insert(0,row)
            var.bind('<Enter>',enter)
            var.bind('<Leave>',leave)
            var.bind('<ButtonRelease-1>',click_chose)
        if self._values:
            for i in self._values:
                button(i)

    def _close_showbox(self,event):
        self.can.destroy()
        self._f_click = False
        self.canvas.itemconfig('f_image',image=self.flash_image_d)

    def _flash_enter(self,event):
        if not self._f_click:
            self.canvas.itemconfig('f_image',image=self.flash_image_d_enter)

    def _flash_Leave(self,event):
        if not self._f_click:
            self.canvas.itemconfig('f_image',image=self.flash_image_d)

    def _flash_click(self,event):
        if self._f_click:
            self._f_click = False
            self.can.destroy()
            self.canvas.itemconfig('f_image',image=self.flash_image_d_enter)
        else:
            self._f_click = True
            self.canvas.itemconfig('f_image',image=self.flash_image_u_enter)
            self._showbox()

    def _set_sizes(self,width,height):
        self._configure_itemes(width=width,height=height)
        self.canvas.configure(width=width,height=height)

    def _mix_colors(self,c1,c2,c1_x=None,c2_x=None):
        return mix_colors(c1,c2,c1_x=c1_x,c2_x=c2_x)

    def destroy(self):
        self._master.configure = self._master_olde_configure
        self._master.config = self._master_olde_configure
        Entry.destroy(self)
        self.canvas.destroy()

    def configure(self,**kwargs):
        if 'bg' in kwargs:
            self._bg =self._mix_colors(kwargs.pop('bg'),self._master_bg,c1_x=self._alpha)
            Drow_angles.configure(self,bg=self._bg)
            self._fg_desible = self._mix_colors(self._fg,self._bg,c1_x=0.3)
            Entry.configure(self,bg=self._bg)
            if self._text == Entry.get(self):
                Entry.configure(self,fg=self._fg_desible)
        if 'outline' in kwargs:
            self._outline = kwargs.pop('outline')
            Drow_angles.configure(self,outline=self._outline)
            self.flash_image_u = icon_to_image('chevron-up',fill=self._outline,scale_to_width =14)
            self.flash_image_d = icon_to_image('chevron-down',fill=self._outline,scale_to_width =14)
            self.canvas.itemconfig('f_image',image=self.flash_image_d)
        if 'outline_focus'in kwargs:
            self._outline_focus = kwargs.pop('outline_focus')
            self.flash_image_u_enter = icon_to_image('chevron-up',fill=self._outline_focus,scale_to_width =14)
            self.flash_image_d_enter = icon_to_image('chevron-down',fill=self._outline_focus,scale_to_width =14)
        if 'font' in kwargs:
            Entry.configure(self,font=kwargs.pop('font'))
            self._bbox_entry()
        if 'fg' in kwargs:
            self._fg=kwargs.pop('fg')
            self._fg_desible = self._mix_colors(self._fg,self._bg,c1_x=0.3)
            if Entry.get(self) == self._text:
                Entry.configure(self,fg=self._fg_desible)
            else:
                Entry.configure(self,fg=self._fg)

    config = configure

    def winfo_width(self):
        return self.canvas.winfo_width()

    def winfo_height(self):
        return self.canvas.winfo_height()
    
    def get(self):
        if Entry.get(self) == self._text:
            return ''
        else:
            return Entry.get(self)

    def destroy(self):
        Entry.destroy(self)
        self.canvas.destroy()

    def pack(self,**kwargs):
        self.canvas.pack(**kwargs)

    def place(self,**kwargs):
        self.canvas.place(**kwargs)
    
    def grid(self,**kwargs):
        self.canvas.grid(**kwargs)

class DB_Connect:
    def connect(db):
        Db=sqlite3.connect(db)
        Db.row_factory=sqlite3.Row
        class config:
            def Tables():
                cursor=Db.cursor()
                cursor.execute('SELECT name from sqlite_master where type= "table"')
                return list(map(lambda x:x[0],cursor))

            def Create_Table(table_name,sql=None):
                try:
                    cursor=Db.cursor()
                    if sql:
                        cursor.execute('CREATE TABLE IF NOT EXISTS {} ({})'.format(table_name,sql))
                    else:
                        cursor.execute('CREATE TABLE IF NOT EXISTS {}'.format(table_name))
                    return True
                except sqlite3.Error as error:
                    return error
            
            def Drop_Table(table_name):
                try:
                    cursor=Db.cursor()
                    cursor.execute('DROP TABLE {}'.format(table_name))
                    return True
                except sqlite3.Error as error:
                    return error

            def Commit():
                Db.commit()

            def close():
                Db.close()
            
            def Open(table):
                Table=StringVar()
                Table.set(table)
                cursor=Db.cursor()
                class config:

                    def Columns_Info():
                        cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' and name=\'{}\'".format(table))
                        sql= list(map(lambda x:x[0],cursor))[0]
                        c1=True
                        c2=True
                        for row in range(len(sql)):
                            if sql[row] == '(' and c1:
                                c1=False
                                ferst_=row
                            if sql[-row] ==')' and c2:
                                c2=False
                                last_=-row
                        the_sql=sql[ferst_+1:last_]
                        info_list=[]
                        info=''
                        for row in the_sql:
                            if row != ',':
                                info+=row
                            else:
                                info_list.append(info)
                                info=''
                        info_list.append(info)
                        the_info=[]
                        for row in info_list:
                            the=[]
                            v=row.split()
                            the.append(v[0])
                            v.pop(0)
                            t=''
                            for row in v:
                                t+=f' {row}'
                            the.append(t)
                            the_info.append(the)
                        return the_info

                    def Columns():
                        cursor.execute('SELECT * FROM '+Table.get())
                        values=list(map(lambda x: x[0],cursor.description))
                        pry_key=''
                        for row in config.Columns_Info():
                            if 'primary key autoincrement' in row[1].lower():
                                pry_key = row[0]
                        if pry_key == '':
                            return [values, None]
                        else:
                            return [values,pry_key]
 
                    def List_Requst():
                        cursor.execute('SELECT * FROM '+Table.get())
                        # return map(lambda x:list(x),cursor)
                        return cursor

                    def Add_Column(sql):
                        try:
                            cursor.execute('ALTER TABLE {} ADD {}'.format(Table.get(),sql))
                            return True
                        except sqlite3.Error as error:
                            return error

                    def Drop_Column(col_name):
                        try:
                            cursor.execute('ALTER TABLE {} DROP {}'.format(Table.get(),col_name))
                            return True
                        except sqlite3.Error as error:
                            return error

                    def Rename_Table(new_name):
                        try:
                            cursor.execute('ALTER TABLE {} RENAME TO {} '.format(Table.get(),new_name))
                            Table.set(new_name)
                            return True
                        except sqlite3.Error as error:
                            return error

                    def Rename_Column(current_name,new_name):
                        try:
                            cursor.execute('ALTER TABLE {} RENAME COLUMN {} TO {} '.format(Table.get(),current_name,new_name))
                            return True
                        except sqlite3.Error as error:
                            return error

                    def Add(columns,values):
                        try:
                            col=''
                            val=''
                            for row in range(len(values)):
                                if row != 0 :
                                    val+=f',\'{values[row]}\''
                                    col+=f',{columns[row]}'
                                elif row == 0:
                                    val+=f'\'{values[0]}\''
                                    col+=f'{columns[0]}'
                            cursor.execute('INSERT INTO {}({}) VALUES ({})'.format(Table.get(),col,val))
                            return True
                        except sqlite3.Error as error:
                            return error

                    def Update(columns,values,where,where_value):
                        try:
                            sets=''
                            for i in range(len(columns)):
                                if i == 0 :
                                    sets+=f'{columns[0]}=\'{values[0]}\''
                                else:
                                    sets+=f',{columns[i]}=\'{values[i]}\''
                            cursor.execute('UPDATE {} set {} where {}=\'{}\''.format(Table.get(),sets,where,where_value))
                            return True
                        except sqlite3.Error as error:
                            return error

                    def Delete(where,where_value):
                        try:
                            w=f'{where}=\'{where_value}\''
                            cursor.execute('DELETE FROM {} WHERE {}'.format(Table.get(),w))
                            return True
                        except sqlite3.Error as error:
                            return error

                    def Search(where,value):
                        cursor.execute('SELECT * FROM {} WHERE {} LIKE \'{}\''.format(Table.get(),where,value))
                        return list(map( lambda x: list(x) , cursor ))

                    def Name():
                        return Table.get()

                    def Commit():
                        Db.commit()

                    def close():
                        Db.close()
                            
                return config
        return config
