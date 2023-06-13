from html import escape


def show_html(game):
    title = f"{game.Name}"

    url_game_hg = f"{game.Url_game_hg}"
    url_game_lavka = f"{game.Url_game_lavka}"
    image_hg = f"{game.Image_HG}"
    slogan = f"{game.Slogan}"
    tags = f"{game.Tags}"
    price = f"{game.Price}"
    players = f"{game.Player}"
    time = f"{game.Time}"
    age = f"{game.Age}"
    year = f"{game.Year}"
    manufactory = f"{game.Manufacture}"
    equipment = f"{game.Equipment}"
    description = f"{game.Description}"
    language = f"{game.Language}"
    image_lavka = f"{game.Image_lavka}"
    rating_bgg = f"{game.Rating_bgg}"
    rating_tesera = f"{game.Rating_tesera}"
    image_gaga = f"{game.Image_gaga}"
    plus = f"{game.Plus}"
    features = f"{game.Feature}"
    minus = f"{game.Minus}"
    resume = f"{game.Resume}"
    rules = f"{game.Rules}"
    url_game_gaga = f"{game.Url_game_gaga}"
    # figure1 = '&#123'
    # figure2 = '&#125'

    # script_path= "C:/Users/ilyan/PycharmProjects/sravni_beri/bot/handlers/users/script.js"
    script = """
    
  // список комплектации
  let strEquipment = '%s';
  let arrEquipment = strEquipment.split(",");


  for (let i = 0; i < arrEquipment.length; i++) {{
    let li = document.createElement("li");
    li.innerHTML = `- ${{arrEquipment[i]}}`;
    document.getElementById("equipmentList").appendChild(li);
  }}
  
  // список плюсов
  let strPlus = '%s';
  let arrPlus = strPlus.split("^");


    if (strPlus !== '') {{
        for (let i = 0; i < arrPlus.length-1; i++) {{
            let li = document.createElement("li");
            li.innerHTML = `<svg style="flex-shrink: 0" class="w-8 h-8 -ml-1" xmlns="http://www.w3.org/2000/svg" width="800px" height="800px" viewBox="0 0 24 24" fill="none">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M11 17C11 17.5523 11.4477 18 12 18C12.5523 18 13 17.5523 13 17V13H17C17.5523 13 18 12.5523 18 12C18 11.4477 17.5523 11 17 11H13V7C13 6.44771 12.5523 6 12 6C11.4477 6 11 6.44771 11 7V11H7C6.44772 11 6 11.4477 6 12C6 12.5523 6.44772 13 7 13H11V17Z" fill="green"/>
                      </svg> ${{arrPlus[i]}}`;
            document.getElementById("plusList").appendChild(li);
            li.classList.add('flex')
            li.classList.add('gap-x-2')
         }}
    }}

  // список минусов
  let strMinus = '%s';
  let arrMinus = strMinus.split("^");

  for (let i = 0; i < arrMinus.length - 1; i++) {{
    let li = document.createElement("li");
    li.innerHTML = `<svg style="flex-shrink: 0" class="w-8 h-8" xmlns="http://www.w3.org/2000/svg" width="600px" height="600px" viewBox="0 0 24 24" fill="none">
                <path fill="red" fill-rule="evenodd" d="M18 10a1 1 0 01-1 1H3a1 1 0 110-2h14a1 1 0 011 1z"/>
              </svg> ${{arrMinus[i]}}`;
    document.getElementById("minusList").appendChild(li);
    li.classList.add('flex')
    li.classList.add('gap-x-2')
  }}

  // список особенностей
  let strFeatures = '%s';
  let arrFeatures = strFeatures.split("^");

  for (let i = 0; i < arrFeatures.length - 1; i++) {{
    let li = document.createElement("li");
    li.innerHTML = `<svg style="flex-shrink: 0" class="w-6 h-8" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.0" id="Layer_1" width="600px" height="600px" viewBox="0 0 64 64" enable-background="new 0 0 64 64" xml:space="preserve">
              <path fill="#FFDC5F" d="M62.799,23.737c-0.47-1.399-1.681-2.419-3.139-2.642l-16.969-2.593L35.069,2.265  C34.419,0.881,33.03,0,31.504,0c-1.527,0-2.915,0.881-3.565,2.265l-7.623,16.238L3.347,21.096c-1.458,0.223-2.669,1.242-3.138,2.642  c-0.469,1.4-0.115,2.942,0.916,4l12.392,12.707l-2.935,17.977c-0.242,1.488,0.389,2.984,1.62,3.854  c1.23,0.87,2.854,0.958,4.177,0.228l15.126-8.365l15.126,8.365c0.597,0.33,1.254,0.492,1.908,0.492c0.796,0,1.592-0.242,2.269-0.72  c1.231-0.869,1.861-2.365,1.619-3.854l-2.935-17.977l12.393-12.707C62.914,26.68,63.268,25.138,62.799,23.737z"/>
            </svg> ${{arrFeatures[i]}}`;
    document.getElementById("featuresList").appendChild(li);
    // li.classList.add('flex items-center gap-x-2')
    li.classList.add('flex')
    li.classList.add('gap-x-2')
  }}
    // скрываем плюсы и минусы, если не пришли плюсы
  if (document.getElementById("plusList").textContent === '') {{
    document.getElementById("plusAndMinus").style.display = "none";
  }}
    
  // скрываем язык, если его нет
  if (document.getElementById("languageText").textContent === '') {{
    document.getElementById("language").style.display = "none";
  }}

  // скрываем слоган, если его нет
  if (document.getElementById("slogan").textContent === '') {{
    document.getElementById("slogan").style.display = "none";
  }}

  // скрываем кол-во игроков, если его нет
  if (document.getElementById("playersText").textContent === '') {{
    document.getElementById("players").style.display = "none";
  }}

  // скрываем время, если его нет
  if (document.getElementById("timeText").textContent === '') {{
    document.getElementById("time").style.display = "none";
  }}

  // скрываем возраст, если его нет
  if (document.getElementById("ageText").textContent === '') {{
    document.getElementById("age").style.display = "none";
  }}

  // скрываем резюме, если его нет
  if (document.getElementById("resumeText").textContent === '') {{
    document.getElementById("resume").style.display = "none";
  }}
  
  // скрываем рейтиниги, если их нет
  if (document.getElementById("ratingBGGText").textContent === '' && document.getElementById("ratingTeseraText").textContent === '') {{
    document.getElementById("ratings").style.display = "none";
  }}
  else if (document.getElementById("ratingBGGText").textContent === '') {{
    document.getElementById("ratingBGG").style.display = "none";
  }}
  else if (document.getElementById("ratingTeseraText").textContent === '') {{
    document.getElementById("ratingTesera").style.display = "none";
  }}

  // скрываем правила, если их нет
  if (document.getElementById("rulesText").href === '') {{
    document.getElementById("rules").style.display = "none";
  }}
  
  // скрываем комплектацию, если ее нет
  if (strEquipment === '') {{
    document.getElementById("equipment").style.display = "none";
  }}
  
  // деление с остатком
  function divideWithoutModulo(dividend, divisor) {{
      while (dividend >= divisor) {{
        dividend -= divisor;
  }}
  return dividend;
}}
  
  const images = ['%s', '%s', '%s'];
    
    const filteredImages = images.filter((item) => {{
    if (item)
      return item
  }})

    let currentImage = 0;
    const carousel = document.querySelector('.carousel');
    const carouselDesktop = document.querySelector('.carousel-desktop');

    if (filteredImages.length === 1) {{
      document.getElementById('prevButton').style.display = 'none'
      document.getElementById('nextButton').style.display = 'none'
    }}
    function showSlide() {{
      carousel.innerHTML = `<img class='h-[400px] w-[400px] object-cover' src='${{filteredImages[currentImage]}}' alt=''>`;
      carouselDesktop.innerHTML = `<img class='h-[400px] w-[400px] object-cover' src='${{filteredImages[currentImage]}}' alt=''>`;
    }}

    function prevSlide() {{
      if (filteredImages[currentImage]) {{
        currentImage = divideWithoutModulo((currentImage - 1 + filteredImages.length), filteredImages.length);
        showSlide();
      }}
      else {{
        currentImage = 0
        showSlide();
      }}
    }}

    function nextSlide() {{
      if (filteredImages[currentImage]) {{
        currentImage =divideWithoutModulo((currentImage + 1), filteredImages.length);
        showSlide();
      }}
      else {{
        currentImage = 0
        showSlide();
      }}
    }}
    showSlide();
  
  """ % (equipment, plus, minus, features,image_hg,image_gaga,image_lavka)

    html = f"""
                    <!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <script src="https://cdn.tailwindcss.com"></script>
  <title>{title}</title>
</head>
<body>
<header class="flex justify-between items-center h-16 shadow-md fixed z-10 w-full px-4 md:px-32 bg-white">
  <p class="text-lg font-bold text-xl">Сравни, бери!</p>
  <div class="flex items-center gap-x-2">
    <a href="https://t.me/sravni_beri_bot" target="_blank"> @sravni_beri_bot</a>
    <a href="https://t.me/sravni_beri_bot" target="_blank">
      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="12" cy="12" r="10.5" fill="url(#paint0_linear_2674_135076)"/>
        <path d="M17.2399 7.65659C17.3334 7.05249 16.7591 6.57567 16.2219 6.8115L5.52361 11.5086C5.13842 11.6778 5.1666 12.2612 5.5661 12.3884L7.77236 13.091C8.19344 13.2251 8.64939 13.1558 9.01709 12.9017L13.9912 9.4652C14.1412 9.36157 14.3047 9.57485 14.1766 9.70697L10.5961 13.3985C10.2488 13.7566 10.3177 14.3634 10.7355 14.6254L14.7442 17.1392C15.1938 17.4212 15.7723 17.1379 15.8564 16.5946L17.2399 7.65659Z" fill="white"/>
        <defs>
          <linearGradient id="paint0_linear_2674_135076" x1="12" y1="1.5" x2="12" y2="22.5" gradientUnits="userSpaceOnUse">
            <stop stop-color="#37BBFE"/>
            <stop offset="1" stop-color="#007DBB"/>
          </linearGradient>
        </defs>
      </svg>
    </a>
  </div>
</header>

<main class="py-24 md:py-32 px-4 md:px-32 text-xl">
  <h1 class="text-5xl font-bold mt-4">{title}</h1>
  <h3 id="slogan" class="text-xl font-semibold mt-4">{slogan}</h3>

  <hr class="my-8">

  <div class="md:flex justify-between gap-x-16">
    <div class="md:hidden block">
      <div class="carousel flex justify-center overflow-hidden w-full">
      </div>
      <div class="flex justify-center mt-4 mb-8">
        <button id="prevButton" onclick="prevSlide()" class="bg-[#0094FF] hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-l">
          Назад
        </button>
        <button id="nextButton" onclick="nextSlide()" class="bg-[#0094FF] hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-r">
          Вперёд
        </button>
      </div>
    </div>

    <div>
      <h2 class="text-3xl font-bold">Цена: <span>{price}</span> ₽</h2>

      <div class="flex gap-x-2 mt-8 ">
        <p class="bg-[#0094FF] py-1 px-3 text-white font-semibold rounded-xl max-h-[36px]">Теги:</p>
        <p class="text-gray-500 mt-1">{tags}</p>
      </div>

      <ul class="mt-8">
        <li id="players" class="flex items-center gap-x-2 text-gray-500 mb-2">
          <svg class="fill-[#0094FF] w-8 h-8"  xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="_x32_" width="800px" height="800px" viewBox="0 0 512 512" xml:space="preserve">
            <g>
	          <path class="st0" d="M147.57,320.188c-0.078-0.797-0.328-1.531-0.328-2.328v-6.828c0-3.25,0.531-6.453,1.594-9.5   c0,0,17.016-22.781,25.063-49.547c-8.813-18.594-16.813-41.734-16.813-64.672c0-5.328,0.391-10.484,0.938-15.563   c-11.484-12.031-27-18.844-44.141-18.844c-35.391,0-64.109,28.875-64.109,73.75c0,35.906,29.219,74.875,29.219,74.875   c1.031,3.047,1.563,6.25,1.563,9.5v6.828c0,8.516-4.969,16.266-12.719,19.813l-46.391,18.953   C10.664,361.594,2.992,371.5,0.852,383.156l-0.797,10.203c-0.406,5.313,1.406,10.547,5.031,14.438   c3.609,3.922,8.688,6.125,14.016,6.125H94.93l3.109-39.953l0.203-1.078c3.797-20.953,17.641-38.766,36.984-47.672L147.57,320.188z"/>
              <path class="st0" d="M511.148,383.156c-2.125-11.656-9.797-21.563-20.578-26.531l-46.422-18.953   c-7.75-3.547-12.688-11.297-12.688-19.813v-6.828c0-3.25,0.516-6.453,1.578-9.5c0,0,29.203-38.969,29.203-74.875   c0-44.875-28.703-73.75-64.156-73.75c-17.109,0-32.625,6.813-44.141,18.875c0.563,5.063,0.953,10.203,0.953,15.531   c0,22.922-7.984,46.063-16.781,64.656c8.031,26.766,25.078,49.563,25.078,49.563c1.031,3.047,1.578,6.25,1.578,9.5v6.828   c0,0.797-0.266,1.531-0.344,2.328l11.5,4.688c20.156,9.219,34,27.031,37.844,47.984l0.188,1.094l3.094,39.969h75.859   c5.328,0,10.406-2.203,14-6.125c3.625-3.891,5.438-9.125,5.031-14.438L511.148,383.156z"/>
              <path class="st0" d="M367.867,344.609l-56.156-22.953c-9.375-4.313-15.359-13.688-15.359-23.969v-8.281   c0-3.906,0.625-7.797,1.922-11.5c0,0,35.313-47.125,35.313-90.594c0-54.313-34.734-89.234-77.594-89.234   c-42.844,0-77.594,34.922-77.594,89.234c0,43.469,35.344,90.594,35.344,90.594c1.266,3.703,1.922,7.594,1.922,11.5v8.281   c0,10.281-6.031,19.656-15.391,23.969l-56.156,22.953c-13.047,5.984-22.344,17.984-24.906,32.109l-2.891,37.203h139.672h139.672   l-2.859-37.203C390.211,362.594,380.914,350.594,367.867,344.609z"/>
            </g>
          </svg>
          <p>Кол-во игроков: </p>
          <p id="playersText">{players}</p>
        </li>
        <li id="age" class="flex items-center gap-x-2 text-gray-500 mb-2">
          <svg class="fill-[#0094FF] w-8 h-6" xmlns="http://www.w3.org/2000/svg" fill="#000000" width="800px" height="800px" viewBox="0 0 32 32" version="1.1">
            <title>plus-user</title>
            <path d="M2.016 28q0 0.832 0.576 1.44t1.408 0.576h14.016v-0.352q-1.792-0.608-2.912-2.176t-1.088-3.488q0-2.016 1.184-3.584t3.072-2.112q0.384-1.216 1.216-2.176t2.016-1.504q0.512-1.376 0.512-2.624v-1.984q0-3.328-2.368-5.664t-5.632-2.336-5.664 2.336-2.336 5.664v1.984q0 2.112 1.024 3.904t2.784 2.912q-1.504 0.544-2.912 1.504t-2.496 2.144-1.76 2.624-0.64 2.912zM18.016 24q0 0.832 0.576 1.44t1.408 0.576h2.016v1.984q0 0.864 0.576 1.44t1.408 0.576 1.408-0.576 0.608-1.44v-1.984h1.984q0.832 0 1.408-0.576t0.608-1.44-0.608-1.408-1.408-0.576h-1.984v-2.016q0-0.832-0.608-1.408t-1.408-0.576-1.408 0.576-0.576 1.408v2.016h-2.016q-0.832 0-1.408 0.576t-0.576 1.408z"/>
          </svg>
          <p>Возраст: </p>
          <p id="ageText">{age}</p>
        </li>
        <li id="time" class="flex items-center gap-x-2 text-gray-500 mb-2">
          <svg class="w-8 h-8" xmlns="http://www.w3.org/2000/svg" width="800px" height="800px" viewBox="0 0 24 24" fill="none">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C7.58172 4 4 7.58172 4 12C4 16.4183 7.58172 20 12 20C16.4183 20 20 16.4183 20 12C20 7.58172 16.4183 4 12 4ZM2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12ZM11.8284 6.75736C12.3807 6.75736 12.8284 7.20507 12.8284 7.75736V12.7245L16.3553 14.0653C16.8716 14.2615 17.131 14.8391 16.9347 15.3553C16.7385 15.8716 16.1609 16.131 15.6447 15.9347L11.4731 14.349C11.085 14.2014 10.8284 13.8294 10.8284 13.4142V7.75736C10.8284 7.20507 11.2761 6.75736 11.8284 6.75736Z" fill="#0094FF"/>
          </svg>
          <p>Время партии: </p>
          <p id="timeText">{time} мин</p>
        </li>
        <li id="language" class="flex items-center gap-x-2 text-gray-500 mb-2">
          <svg class="w-8 h-8" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#0094FF" width="800px" height="800px" viewBox="0 0 36 36" version="1.1" preserveAspectRatio="xMidYMid meet">
            <title>language-solid</title>
            <polygon points="11,16.5 10,19.6 12,19.6 11,16.5  " class="clr-i-solid clr-i-solid-path-1"/><path d="M30.3,3h-16v5h4v2h-13c-1.7,0-3,1.3-3,3v11c0,1.7,1.3,3,3,3h1v5.1l6.3-5.1h6.7v-7h11c1.7,0,3-1.3,3-3V6   C33.3,4.3,32,3,30.3,3z M13.1,22.9l-0.5-1.6H9.5l-0.6,1.6H6.5L9.8,14h2.4l3.3,8.9L13.1,22.9z M28.3,15v2c-1.3,0-2.7-0.4-3.9-1   c-1.2,0.6-2.6,0.9-4,1l-0.1-2c0.7,0,1.4-0.1,2.1-0.3c-0.9-0.9-1.5-2-1.8-3.2h2.1c0.3,0.9,0.9,1.6,1.6,2.2c1.1-0.9,1.8-2.2,1.9-3.7   h-6V8h3V6h2v2h3.3l0.1,1c0.1,2.1-0.7,4.2-2.2,5.7C27.1,14.9,27.7,15,28.3,15z" class="clr-i-solid clr-i-solid-path-2"/>
            <rect x="0" y="0" width="36" height="36" fill-opacity="0"/>
          </svg>
          <p>Язык: </p>
          <p id="languageText">{language}</p>
        </li>
        <li class="flex items-center gap-x-2 text-gray-500 mb-2">
          <svg class="w-8 h-8" xmlns="http://www.w3.org/2000/svg" width="800px" height="800px" viewBox="0 0 24 24" fill="none">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M12 8.00002C9.79085 8.00002 7.99999 9.79088 7.99999 12C7.99999 14.2092 9.79085 16 12 16C14.2091 16 16 14.2092 16 12C16 9.79088 14.2091 8.00002 12 8.00002ZM9.99999 12C9.99999 10.8955 10.8954 10 12 10C13.1046 10 14 10.8955 14 12C14 13.1046 13.1046 14 12 14C10.8954 14 9.99999 13.1046 9.99999 12Z" fill="#0094FF"/>
            <path fill-rule="evenodd" clip-rule="evenodd" d="M12 8.00002C9.79085 8.00002 7.99999 9.79088 7.99999 12C7.99999 14.2092 9.79085 16 12 16C14.2091 16 16 14.2092 16 12C16 9.79088 14.2091 8.00002 12 8.00002ZM9.99999 12C9.99999 10.8955 10.8954 10 12 10C13.1046 10 14 10.8955 14 12C14 13.1046 13.1046 14 12 14C10.8954 14 9.99999 13.1046 9.99999 12Z" fill="#0094FF"/>
            <path fill-rule="evenodd" clip-rule="evenodd" d="M10.7673 1.01709C10.9925 0.999829 11.2454 0.99993 11.4516 1.00001L12.5484 1.00001C12.7546 0.99993 13.0075 0.999829 13.2327 1.01709C13.4989 1.03749 13.8678 1.08936 14.2634 1.26937C14.7635 1.49689 15.1915 1.85736 15.5007 2.31147C15.7454 2.67075 15.8592 3.0255 15.9246 3.2843C15.9799 3.50334 16.0228 3.75249 16.0577 3.9557L16.1993 4.77635L16.2021 4.77788C16.2369 4.79712 16.2715 4.81659 16.306 4.8363L16.3086 4.83774L17.2455 4.49865C17.4356 4.42978 17.6693 4.34509 17.8835 4.28543C18.1371 4.2148 18.4954 4.13889 18.9216 4.17026C19.4614 4.20998 19.9803 4.39497 20.4235 4.70563C20.7734 4.95095 21.0029 5.23636 21.1546 5.4515C21.2829 5.63326 21.4103 5.84671 21.514 6.02029L22.0158 6.86003C22.1256 7.04345 22.2594 7.26713 22.3627 7.47527C22.4843 7.7203 22.6328 8.07474 22.6777 8.52067C22.7341 9.08222 22.6311 9.64831 22.3803 10.1539C22.1811 10.5554 21.9171 10.8347 21.7169 11.0212C21.5469 11.1795 21.3428 11.3417 21.1755 11.4746L20.5 12L21.1755 12.5254C21.3428 12.6584 21.5469 12.8205 21.7169 12.9789C21.9171 13.1653 22.1811 13.4446 22.3802 13.8461C22.631 14.3517 22.7341 14.9178 22.6776 15.4794C22.6328 15.9253 22.4842 16.2797 22.3626 16.5248C22.2593 16.7329 22.1255 16.9566 22.0158 17.14L21.5138 17.9799C21.4102 18.1535 21.2828 18.3668 21.1546 18.5485C21.0028 18.7637 20.7734 19.0491 20.4234 19.2944C19.9803 19.6051 19.4613 19.7901 18.9216 19.8298C18.4954 19.8612 18.1371 19.7852 17.8835 19.7146C17.6692 19.6549 17.4355 19.5703 17.2454 19.5014L16.3085 19.1623L16.306 19.1638C16.2715 19.1835 16.2369 19.2029 16.2021 19.2222L16.1993 19.2237L16.0577 20.0443C16.0228 20.2475 15.9799 20.4967 15.9246 20.7157C15.8592 20.9745 15.7454 21.3293 15.5007 21.6886C15.1915 22.1427 14.7635 22.5032 14.2634 22.7307C13.8678 22.9107 13.4989 22.9626 13.2327 22.983C13.0074 23.0002 12.7546 23.0001 12.5484 23H11.4516C11.2454 23.0001 10.9925 23.0002 10.7673 22.983C10.5011 22.9626 10.1322 22.9107 9.73655 22.7307C9.23648 22.5032 8.80849 22.1427 8.49926 21.6886C8.25461 21.3293 8.14077 20.9745 8.07542 20.7157C8.02011 20.4967 7.97723 20.2475 7.94225 20.0443L7.80068 19.2237L7.79791 19.2222C7.7631 19.2029 7.72845 19.1835 7.69396 19.1637L7.69142 19.1623L6.75458 19.5014C6.5645 19.5702 6.33078 19.6549 6.11651 19.7146C5.86288 19.7852 5.50463 19.8611 5.07841 19.8298C4.53866 19.7901 4.01971 19.6051 3.57654 19.2944C3.2266 19.0491 2.99714 18.7637 2.84539 18.5485C2.71718 18.3668 2.58974 18.1534 2.4861 17.9798L1.98418 17.14C1.87447 16.9566 1.74067 16.7329 1.63737 16.5248C1.51575 16.2797 1.36719 15.9253 1.32235 15.4794C1.26588 14.9178 1.36897 14.3517 1.61976 13.8461C1.81892 13.4446 2.08289 13.1653 2.28308 12.9789C2.45312 12.8205 2.65717 12.6584 2.82449 12.5254L3.47844 12.0054V11.9947L2.82445 11.4746C2.65712 11.3417 2.45308 11.1795 2.28304 11.0212C2.08285 10.8347 1.81888 10.5554 1.61972 10.1539C1.36893 9.64832 1.26584 9.08224 1.3223 8.52069C1.36714 8.07476 1.51571 7.72032 1.63732 7.47528C1.74062 7.26715 1.87443 7.04347 1.98414 6.86005L2.48605 6.02026C2.58969 5.84669 2.71714 5.63326 2.84534 5.45151C2.9971 5.23637 3.22655 4.95096 3.5765 4.70565C4.01966 4.39498 4.53862 4.20999 5.07837 4.17027C5.50458 4.1389 5.86284 4.21481 6.11646 4.28544C6.33072 4.34511 6.56444 4.4298 6.75451 4.49867L7.69141 4.83775L7.69394 4.8363C7.72844 4.8166 7.7631 4.79712 7.79791 4.77788L7.80068 4.77635L7.94225 3.95571C7.97723 3.7525 8.02011 3.50334 8.07542 3.2843C8.14077 3.0255 8.25461 2.67075 8.49926 2.31147C8.80849 1.85736 9.23648 1.49689 9.73655 1.26937C10.1322 1.08936 10.5011 1.03749 10.7673 1.01709ZM14.0938 4.3363C14.011 3.85634 13.9696 3.61637 13.8476 3.43717C13.7445 3.2858 13.6019 3.16564 13.4352 3.0898C13.2378 3.00002 12.9943 3.00002 12.5073 3.00002H11.4927C11.0057 3.00002 10.7621 3.00002 10.5648 3.0898C10.3981 3.16564 10.2555 3.2858 10.1524 3.43717C10.0304 3.61637 9.98895 3.85634 9.90615 4.3363L9.75012 5.24064C9.69445 5.56333 9.66662 5.72467 9.60765 5.84869C9.54975 5.97047 9.50241 6.03703 9.40636 6.13166C9.30853 6.22804 9.12753 6.3281 8.76554 6.52822C8.73884 6.54298 8.71227 6.55791 8.68582 6.57302C8.33956 6.77078 8.16643 6.86966 8.03785 6.90314C7.91158 6.93602 7.83293 6.94279 7.70289 6.93196C7.57049 6.92094 7.42216 6.86726 7.12551 6.7599L6.11194 6.39308C5.66271 6.2305 5.43809 6.14921 5.22515 6.16488C5.04524 6.17811 4.87225 6.23978 4.72453 6.34333C4.5497 6.46589 4.42715 6.67094 4.18206 7.08103L3.72269 7.84965C3.46394 8.2826 3.33456 8.49907 3.31227 8.72078C3.29345 8.90796 3.32781 9.09665 3.41141 9.26519C3.51042 9.4648 3.7078 9.62177 4.10256 9.9357L4.82745 10.5122C5.07927 10.7124 5.20518 10.8126 5.28411 10.9199C5.36944 11.036 5.40583 11.1114 5.44354 11.2504C5.47844 11.379 5.47844 11.586 5.47844 12C5.47844 12.414 5.47844 12.621 5.44354 12.7497C5.40582 12.8887 5.36944 12.9641 5.28413 13.0801C5.20518 13.1875 5.07927 13.2876 4.82743 13.4879L4.10261 14.0643C3.70785 14.3783 3.51047 14.5352 3.41145 14.7349C3.32785 14.9034 3.29349 15.0921 3.31231 15.2793C3.33461 15.501 3.46398 15.7174 3.72273 16.1504L4.1821 16.919C4.4272 17.3291 4.54974 17.5342 4.72457 17.6567C4.8723 17.7603 5.04528 17.8219 5.2252 17.8352C5.43813 17.8508 5.66275 17.7695 6.11199 17.607L7.12553 17.2402C7.42216 17.1328 7.5705 17.0791 7.7029 17.0681C7.83294 17.0573 7.91159 17.064 8.03786 17.0969C8.16644 17.1304 8.33956 17.2293 8.68582 17.427C8.71228 17.4421 8.73885 17.4571 8.76554 17.4718C9.12753 17.6719 9.30853 17.772 9.40635 17.8684C9.50241 17.963 9.54975 18.0296 9.60765 18.1514C9.66662 18.2754 9.69445 18.4367 9.75012 18.7594L9.90615 19.6637C9.98895 20.1437 10.0304 20.3837 10.1524 20.5629C10.2555 20.7142 10.3981 20.8344 10.5648 20.9102C10.7621 21 11.0057 21 11.4927 21H12.5073C12.9943 21 13.2378 21 13.4352 20.9102C13.6019 20.8344 13.7445 20.7142 13.8476 20.5629C13.9696 20.3837 14.011 20.1437 14.0938 19.6637L14.2499 18.7594C14.3055 18.4367 14.3334 18.2754 14.3923 18.1514C14.4502 18.0296 14.4976 17.963 14.5936 17.8684C14.6915 17.772 14.8725 17.6719 15.2344 17.4718C15.2611 17.4571 15.2877 17.4421 15.3141 17.427C15.6604 17.2293 15.8335 17.1304 15.9621 17.0969C16.0884 17.064 16.167 17.0573 16.2971 17.0681C16.4295 17.0791 16.5778 17.1328 16.8744 17.2402L17.888 17.607C18.3372 17.7696 18.5619 17.8509 18.7748 17.8352C18.9547 17.8219 19.1277 17.7603 19.2754 17.6567C19.4502 17.5342 19.5728 17.3291 19.8179 16.919L20.2773 16.1504C20.536 15.7175 20.6654 15.501 20.6877 15.2793C20.7065 15.0921 20.6721 14.9034 20.5885 14.7349C20.4895 14.5353 20.2921 14.3783 19.8974 14.0643L19.1726 13.4879C18.9207 13.2876 18.7948 13.1875 18.7159 13.0801C18.6306 12.9641 18.5942 12.8887 18.5564 12.7497C18.5215 12.6211 18.5215 12.414 18.5215 12C18.5215 11.586 18.5215 11.379 18.5564 11.2504C18.5942 11.1114 18.6306 11.036 18.7159 10.9199C18.7948 10.8126 18.9207 10.7124 19.1725 10.5122L19.8974 9.9357C20.2922 9.62176 20.4896 9.46479 20.5886 9.26517C20.6722 9.09664 20.7065 8.90795 20.6877 8.72076C20.6654 8.49906 20.5361 8.28259 20.2773 7.84964L19.8179 7.08102C19.5728 6.67093 19.4503 6.46588 19.2755 6.34332C19.1277 6.23977 18.9548 6.1781 18.7748 6.16486C18.5619 6.14919 18.3373 6.23048 17.888 6.39307L16.8745 6.75989C16.5778 6.86725 16.4295 6.92093 16.2971 6.93195C16.167 6.94278 16.0884 6.93601 15.9621 6.90313C15.8335 6.86965 15.6604 6.77077 15.3142 6.57302C15.2877 6.55791 15.2611 6.54298 15.2345 6.52822C14.8725 6.3281 14.6915 6.22804 14.5936 6.13166C14.4976 6.03703 14.4502 5.97047 14.3923 5.84869C14.3334 5.72467 14.3055 5.56332 14.2499 5.24064L14.0938 4.3363Z" fill="#0094FF"/>
          </svg>
          <p>Производитель:</p>
          <p>{manufactory}</p>
        </li>
        <li class="flex items-center gap-x-2 text-gray-500 mb-2">
          <svg class="w-8 h-8" xmlns="http://www.w3.org/2000/svg" fill="#0094FF" width="800px" height="800px" viewBox="0 0 16 16"><path d="M14.25 2.5h-.75v-1h-1.25v1h-8.5v-1H2.5v1h-.75A1.25 1.25 0 0 0 .5 3.75v9.5a1.25 1.25 0 0 0 1.25 1.25h12.5a1.25 1.25 0 0 0 1.25-1.25v-9.5a1.25 1.25 0 0 0-1.25-1.25zM1.75 3.75h12.5V5H1.75V3.75zm0 9.5v-7h12.5v7z"/><path d="M3 8h1.1v1.2H3zm0 2.4h1.1v1.2H3zM11.8 8h1.1v1.2h-1.1zm0 2.4h1.1v1.2h-1.1zM9.6 8h1.1v1.2H9.6zm0 2.4h1.1v1.2H9.6zM7.4 8h1.1v1.2H7.4zm0 2.4h1.1v1.2H7.4zM5.2 8h1.1v1.2H5.2zm0 2.4h1.1v1.2H5.2z"/></svg>
          <p>Год выпуска: </p>
          <p>{year}</p>
        </li>
      </ul>

      <div id="ratings" class="mt-8 text-gray-500 md:flex items-center gap-x-10">
        <div id="ratingBGG" class="flex items-center gap-x-2 mb-4 md:mb-0">
          <p>Rating BGG: </p>
          <div id="ratingBGGText" class="border border-4 border-[#FFDC5F] rounded-xl font-bold px-2">{rating_bgg}</div>
        </div>
        <div id="ratingTesera" class="flex items-center gap-x-2">
          <p>Rating ТЕСЕРА </p>
          <div id="ratingTeseraText" class="border border-4 border-[#FFDC5F] rounded-xl font-bold px-2">{rating_tesera}</div>
        </div>
      </div>

      <div>
        <h2 class="text-3xl font-bold mt-8 md:mt-16">Описание:</h2>
        <p class="text-gray-500 mt-8">{description}</p>
      </div>

      <div id="plusAndMinus">
        <h2 class="text-3xl font-bold mt-8 md:mt-16">Плюсы и минусы:</h2>
        <div class="mt-8">
          <div>
            <div class="flex items-center gap-x-2 mt-4 md:mt-4">
              <p>Плюсы:</p>
            </div>
            <ul id="plusList" class="text-gray-500 mt-4"></ul>
          </div>

          <div class="md:block w-[1px] border-r border-[#e5e7eb]"></div>

          <div>
            <div class="flex items-center gap-x-2 mt-4 md:mt-4">
              <p>Особенности:</p>
            </div>
            <ul id="featuresList" class="text-gray-500 mt-4"></ul>
          </div>

          <div class="md:block w-[1px] border-r border-[#e5e7eb]"></div>

          <div>
            <div class="flex items-center gap-x-2 mt-4 md:mt-4">
              <p>Минусы:</p>
            </div>
            <ul id="minusList" class="text-gray-500 mt-4"></ul>
          </div>
        </div>
      </div>

      <div id="resume">
        <h2 class="text-3xl font-bold mt-8 md:mt-16">Резюме:</h2>
        <p id="resumeText" class="text-gray-500 mt-8">{resume}</p>
      </div>

      <div id="equipment">
        <h2 class="text-3xl font-bold mt-8 md:mt-16">Комплектация:</h2>
        <ul id="equipmentList" class="text-gray-500 mt-8"></ul>
      </div>

      <div id="rules">
        <h2 class="text-3xl font-bold mt-8 md:mt-16 mb-8">Правила: </h2>
        <a id="rulesText" href="{rules}" target="_blank" class="text-gray-500 hover:text-[#0094FF] transition">Правила игры в PDF</a>
      </div>

      <div>
        <h2 class="text-3xl font-bold mt-8 md:mt-16">Ссылки на игру: </h2>
        <ul id="priceList" class="text-gray-500 mt-8">
          <li class="flex items-center gap-x-2 mb-4">
            <a href="{url_game_gaga}" target="_blank" class="hover:text-[#0094FF] transition">Gaga.ru</a>
            <img class="w-6 h-6" src="https://gaga.ru/favicon.ico" alt="">
          </li>
          <li class="flex items-center gap-x-2 mb-4">
            <a href="{url_game_hg}" target="_blank" class="hover:text-[#0094FF] transition">Hobbygames.ru</a>
            <img class="w-6 h-6" src="https://hobbygames.ru/assets/img/favicons/favicon.ico" alt="">
          </li>
          <li class="flex items-center gap-x-2 mb-4">
            <a href="{url_game_lavka}" target="_blank" class="hover:text-[#0094FF] transition">Lavkaigr.ru</a>
            <img class="w-6 h-6" src="https://www.lavkaigr.ru/media/static/favicon.png" alt="">
          </li>
        </ul>
      </div>
      
    </div>
    
    <div class="hidden md:block min-w-fit">
      <div class="carousel-desktop flex overflow-hidden w-full">
      </div>
      <div class="flex justify-center mt-4">
        <button id="prevButton" onclick="prevSlide()" class="bg-[#0094FF] hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-l">
          Назад
        </button>
        <button id="nextButton" onclick="nextSlide()" class="bg-[#0094FF] hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-r">
          Вперёд
        </button>
      </div>
    </div>

  </div>
</main>

<script>
{script}
</script>
    
</body>
</html>
                    """.format(title=escape(title), url_game_hg=escape(url_game_hg),
                               url_game_lavka=escape(url_game_lavka), slogan=escape(slogan), tags=escape(tags),
                               price=escape(price), players=escape(players), time=escape(time), age=escape(age),
                               year=escape(year), manufactory=escape(manufactory), description=escape(description),
                               language=escape(language), rating_bgg=escape(rating_bgg),
                               rating_tesera=escape(rating_tesera), resume=escape(resume), rules=escape(rules),
                               url_game_gaga=escape(url_game_gaga),script=escape(script))

    with open(f"{game.Name}.html", 'w', encoding="utf-8", errors='ignore') as file:
        file.write(html)
