<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <title>WeatherApp</title>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">WeatherApp</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item dropdown">
              <!-- <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Dropdown
                </a> -->
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled">Disabled</a>
              </li>
            </ul>
            <!-- <form class="d-flex">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form> -->
          </div>
        </div>
      </nav>

      <!-- image bg -->
<div
class="bg-image p-5 text-center shadow-1-strong rounded mb-5 text-white"
style="background-image: url('https://mdbcdn.b-cdn.net/img/new/slides/003.webp');"
>
<h1 class="mb-3 h2">Weather App</h1>

<p>
  
Humidity, air temperature and pressure, wind speed and direction, cloud cover and type, and the amount and form of precipitation are all atmospheric characteristics of the momentary conditions we call weather.


</p>
</div>
<!-- image bg -->
      <div class="container">
    <h1>Weather App </h1>
    <form  action="/" method="POST">
        <div class="mb-3">
          <label  class="form-label">Enter Your City Name</label>
          <input type="text" class="form-control" name="city" aria-describedby="emailHelp">
   
        </div>
       
        
        <button type="submit" class="btn btn-primary btn-lg btn-block">Submit</button> 
      <!-- <button type="button" class="btn btn-primary btn-lg btn-block">Submit</button>-->
        
      </form>





      
      <div class="row justify-content-center">
        <div class="col-md-6 col-sm-12 col-xs-12 pt-5">
            <div class="card border-0 p3 shadow-sm text-center">
                <i class="fa fa-cloud" style="font-size:60px"></i>
                <h3 class="text-muted">Current Weather for {{city}}</h3>
                <h5 class="text-muted">Temperature: {{ temp }} ??C</h5>
                <h5 class="text-muted">Pressure: {{pressure }} hPa</h5>
                <h5 class="text-muted">Humidity: {{ humidity }} %</h5>
                <h5 class="text-muted">Sunrise: {{ sunrise }} AM</h5>
                <h5 class="text-muted">Sunset: {{ sunset }} PM</h5>

             
                

            </div>

        </div>
</div>
</div>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
    -->
    <div>
      <footer class="bg-light text-center text-lg-start">
        <!-- Grid container -->
        <div class="container p-4">
        
        <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
          ?? 2022 Copyright

          <a class="text-dark" href="#">Vivek kumar jha </a>
        </div>
       
      </footer>

    </div>

  </body>
</html>
