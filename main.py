import os
import string
import shutil
import fontforge



# gets us chrs we think are valid to replace
validChr = string.ascii_letters + '?/:!.@#$%^&*()_-+=[]{}<>,1234567890"" '

def generateFonts(originalFont, outputDir='fonts'):
    tmpFont = "temp.ttf"

    font = fontforge.open(originalFont)
    font.save(tmpFont)
    
    refFont = fontforge.open(tmpFont)
    
    for i in range(len(validChr)):
        for char in validChr:
            refLetter = validChr[(validChr.index(char) + i) % len(validChr)]
            refFont.selection.select(refLetter)
            refFont.copy()
            
            fLetter = char
            font.selection.select(fLetter)
            font.paste()
        
        if not os.path.exists(outputDir):
            os.makedirs(outputDir)
        oFile = os.path.join(outputDir, f'{i}.woff')
        font.generate(oFile)
    
    refFont.close()
    font.close()
    os.remove(tmpFont)
    
# generates a css file that you reference to access changed fonts
def generateCSS(CSSFileName):
    with open(CSSFileName, "w") as CSSFile:
        for i in range(len(validChr)):
            fontName = str(i)
            fontUrl = f"fonts/{i}.woff"
            CSS = f"@font-face {{ font-family: \"{fontName}\"; src: url(\"{fontUrl}\") format('woff'); }}"
            CSSFile.write(CSS)
            
            
# gens the code you add to your html
def generateHTML(hiddenText, visibleText):
    finalSpan = ""

    for hiddenChr, visibleChr in zip(hiddenText, visibleText):
        wIndex = validChr.index(hiddenChr)
        sIndex = validChr.index(visibleChr)

        if wIndex <= sIndex:
            font_family = str(abs(wIndex - sIndex))
        else:
            font_family = str(sIndex - wIndex + len(validChr))

        span = f"<span style=\"font-family: '{font_family}';\">{hiddenChr}</span>"
        finalSpan += span

    return finalSpan


if __name__ == "__main__":
    print(r"""

    ███████╗ ██████╗ ███╗   ██╗████████╗██████╗  ██████╗  ██████╗ █████╗ ██╗  ██╗   ██╗██████╗ ███████╗███████╗
    ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝██╔══██╗██║  ╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝
    █████╗  ██║   ██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║     ███████║██║   ╚████╔╝ ██████╔╝███████╗█████╗  
    ██╔══╝  ██║   ██║██║╚██╗██║   ██║   ██╔═══╝ ██║   ██║██║     ██╔══██║██║    ╚██╔╝  ██╔═══╝ ╚════██║██╔══╝  
    ██║     ╚██████╔╝██║ ╚████║   ██║   ██║     ╚██████╔╝╚██████╗██║  ██║███████╗██║   ██║     ███████║███████╗
    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝     ╚══════╝╚══════╝
    made by github.com/anger
    valid chrs: \?\/\:\!\.\@\#\$\%\^\&\*\(\)\_\-\+\=\[\]\{\}\<\>\,1234567890                                                                                                                                                                                                                                                  
    """)
    
    # Allows for user input
    baseFont = input("Enter the base font file: ")
    cssName = input("Enter the CSS file name: ")
    toWrite = input("Enter the text to write: ")
    toSee = input("Enter the text to see: ")
    
    
    # Generates fonts and the css
    generateFonts(baseFont)
    generateCSS(cssName)
    
    
    
    # fun ascii art stuff, debating removing it. 

    print(r"""

    ▄████████  ▄██████▄  ███▄▄▄▄       ███        ▄███████▄  ▄██████▄   ▄████████    ▄████████  ▄█       ▄██   ▄      ▄███████▄    ▄████████    ▄████████ 
    ███    ███ ███    ███ ███▀▀▀██▄ ▀█████████▄   ███    ███ ███    ███ ███    ███   ███    ███ ███       ███   ██▄   ███    ███   ███    ███   ███    ███ 
    ███    █▀  ███    ███ ███   ███    ▀███▀▀██   ███    ███ ███    ███ ███    █▀    ███    ███ ███       ███▄▄▄███   ███    ███   ███    █▀    ███    █▀  
    ▄███▄▄▄     ███    ███ ███   ███     ███   ▀   ███    ███ ███    ███ ███          ███    ███ ███       ▀▀▀▀▀▀███   ███    ███   ███         ▄███▄▄▄     
    ▀▀███▀▀▀     ███    ███ ███   ███     ███     ▀█████████▀  ███    ███ ███        ▀███████████ ███       ▄██   ███ ▀█████████▀  ▀███████████ ▀▀███▀▀▀     
    ███        ███    ███ ███   ███     ███       ███        ███    ███ ███    █▄    ███    ███ ███       ███   ███   ███                 ███   ███    █▄  
    ███        ███    ███ ███   ███     ███       ███        ███    ███ ███    ███   ███    ███ ███▌    ▄ ███   ███   ███           ▄█    ███   ███    ███ 
    ███         ▀██████▀   ▀█   █▀     ▄████▀    ▄████▀       ▀██████▀  ████████▀    ███    █▀  █████▄▄██  ▀█████▀   ▄████▀       ▄████████▀    ██████████ 
                                                                                                ▀                                                          
                                                                                                                                                                                                                                                        
    """)
    print(r"""

    ·▄▄▄       ▐ ▄ ▄▄▄▄▄ ▄▄▄·       ▄▄·  ▄▄▄· ▄▄▌   ▄· ▄▌ ▄▄▄·.▄▄ · ▄▄▄ .
    ▐▄▄·▪     •█▌▐█•██  ▐█ ▄█▪     ▐█ ▌▪▐█ ▀█ ██•  ▐█▪██▌▐█ ▄█▐█ ▀. ▀▄.▀·
    ██▪  ▄█▀▄ ▐█▐▐▌ ▐█.▪ ██▀· ▄█▀▄ ██ ▄▄▄█▀▀█ ██▪  ▐█▌▐█▪ ██▀·▄▀▀▀█▄▐▀▀▪▄
    ██▌.▐█▌.▐▌██▐█▌ ▐█▌·▐█▪·•▐█▌.▐▌▐███▌▐█ ▪▐▌▐█▌▐▌ ▐█▀·.▐█▪·•▐█▄▪▐█▐█▄▄▌
    ▀▀▀  ▀█▄▀▪▀▀ █▪ ▀▀▀ .▀    ▀█▄▀▪·▀▀▀  ▀  ▀ .▀▀▀   ▀ • .▀    ▀▀▀▀  ▀▀▀ 
                                                                                                                                                                                                                                                        
    """)
    print(r"""

    ▄████  ████▄    ▄     ▄▄▄▄▀ █ ▄▄  ████▄ ▄█▄    ██   █    ▀▄    ▄ █ ▄▄    ▄▄▄▄▄   ▄███▄   
    █▀   ▀ █   █     █ ▀▀▀ █    █   █ █   █ █▀ ▀▄  █ █  █      █  █  █   █  █     ▀▄ █▀   ▀  
    █▀▀    █   █ ██   █    █    █▀▀▀  █   █ █   ▀  █▄▄█ █       ▀█   █▀▀▀ ▄  ▀▀▀▀▄   ██▄▄    
    █      ▀████ █ █  █   █     █     ▀████ █▄  ▄▀ █  █ ███▄    █    █     ▀▄▄▄▄▀    █▄   ▄▀ 
    █           █  █ █  ▀       █          ▀███▀     █     ▀ ▄▀      █              ▀███▀   
    ▀          █   ██           ▀                  █                 ▀                     
                                                    ▀                                                                                                                                                                                                                                                                                            
    """)
    print(r"""
    ┌─┐┌─┐┌┐┌┌┬┐┌─┐┌─┐┌─┐┌─┐┬ ┬ ┬┌─┐┌─┐┌─┐
    ├┤ │ ││││ │ ├─┘│ ││  ├─┤│ └┬┘├─┘└─┐├┤ 
    └  └─┘┘└┘ ┴ ┴  └─┘└─┘┴ ┴┴─┘┴ ┴  └─┘└─┘
    made by github.com/anger                                                                                                                                                                                                                                                
    """)
    print("Link your page to the proper css: ")
    print(f'<link rel="stylesheet" href="{cssName}">')
    print("\n")
    # outputs html code to put on your page
    print("Swapped text HTML: ")
    print(generateHTML(toWrite, toSee))