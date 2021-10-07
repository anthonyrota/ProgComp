html = open("index.svg", "x")
html.write("""
<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20001102//EN" 
 "http://www.w3.org/TR/2000/CR-SVG-20001102/DTD/svg-20001102.dtd"> 

<svg width="370" height="370"
     xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink">

<defs>
  <style type="text/css">
  <![CDATA[

    text.C { text-anchor:middle; color: #940000; }   /* centred */
    text.R { text-anchor:end; }      /* right-justified */
    text.title { color: #940000; font-size:17px; font-family:Arial,Helvetica,sansserif; font-weight:bold;  }

    .bar { stroke:#888888; stroke-width:0.5px; }
    .unordered { fill:#FFFD96; stroke:#000000; }
    .secondsquare { fill:#808080 }
    .firstsquare { fill:#FFFFF0}

    .sep { stroke:#444444; stroke-width:0.8px; stroke-dasharray:5,3; }
    .border { stroke: #AAAAAA; stroke-width:4px; fill:#363737; }

    .pink { fill:#FFFD96; }
    .skyblue { fill:#FFFD96; }
  ]]>
  </style>



<rect id="s1" class="firstsquare" filter="url(#bevel)" x="25.0" y="25" width="320" height="320">
</rect>
<rect id="s2" class="secondsquare" filter="url(#bevel)" x="25.0" y="25" width="320" height="320">
</rect> 

""")
