from ezkey import getkey
import requests
import os
import webbrowser


filename = 'spacepics.html'
CWD = os.getcwd()
START_DATE =  "2019-8-01"
END_DATE = "2019-09-01"

# You can get your free NASA API key at https://api.nasa.gov/
API_KEY = getkey("nasa_apod")

selection = input("\nRun NASA slideshow? y/n: ")
if (selection == 'n' or selection == 'N'):
  quit()

request = requests.get(
    f'https://api.nasa.gov/planetary/apod?start_date={START_DATE}&end_date={END_DATE}&api_key={API_KEY}'
    )
items = request.json()

spaceUrls = []
for item in items:
  spaceUrls.append(item['url'])

message = """
  <html>
    <head>
    <style>
      body{
        background: linear-gradient(#e66465, #9198e5);
      }
      img {
        width: 80%;
        display:block;
        margin:auto;
      }
      .fade {
        animation: fadein 1s;
        }
        @keyframes fadein {
          from {
            opacity:0;
          }
          to {
            opacity:1;
          }
        }
    </style>
    </head>
    <body>
      <div id='photo'></div>
      <script>
        var spaceImgs = """ + str(spaceUrls) + """;
        var container = document.getElementById('photo');
        (function(){
          container.innerHTML = '<img src="'+spaceImgs[0]+'" class="fade">';
          var count = 1;
          setInterval(function(){
            var newImg = '<img src="'+spaceImgs[count]+'" class="fade">';
            container.innerHTML = newImg;
            if (count < spaceImgs.length - 1){
              count++;
            }else{
              count = 0;
            }
          }, 4000);
          }());
      </script>
    </body>
  </html>
"""

f = open(filename, 'w')
f.write(message)
f.close()

pathname = 'file://' + CWD + f"/{filename}"

print("CWD - ", pathname)
webbrowser.open_new_tab(pathname)
