##########################################################################################
# filename: movie_project.py
# description: This program creates a simple website that displays a movies poster,
#       gives some info, and plays the trailer
# Required Files: movie.py, play.png
##########################################################################################

import webbrowser
import os.path
import movie

# The following is the html code to create the head of the web page
web_template_head = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Movie Website</title>
        
        <!-- Include all the bootstrap scripts and style sheets -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <style type="text/css" media="screen">
            .content {{
                position: relative;
                height: 260px;
            }}
            .bottom-align-text {{
                position: absolute;
                bottom: 0;
            }}
        </style>
        <script type="text/javascript">
            $(document).ready(function(){{
                {web_template_modal_script}
            }});
        </script>
        
  </head>
'''

# The following is the html code to create the body of the web page
web_template_body = '''
    <!DOCTYPE html>
    <html lang="en">
        <body>
        <nav class="navbar navbar-inverse">
            <div class="container-fluid">
                <div class="navbar-header">
                    <p class="navbar-brand">Movie Website</p>
                </div>
                <u1 class="nav navbar-nav">
                    <li class="active"><a href="#">Movies</a></li>
                </u1>
            </div>
        </nav>

        {modal_content}
        
        <div class="container-fluid">
          {movie_content}
        </div>
      </body>
    </html>
'''

# The following is the code necessary to stop the video playback when the modal is closed
modal_script = '''
                // Get the current url for the youtube video before removing it.
                var url_{trailer_web_id} = $("#{trailer_web_id}").attr('src');
                
                // Delete the URL or set it to ''
                $("#{modal_web_id}").on('hide.bs.modal', function(){{

                    $("#{trailer_web_id}").attr('src', '');
                }});
                
                // Set the youtube URL when the modal is shown
                $("#{modal_web_id}").on('show.bs.modal', function(){{
                    $("#{trailer_web_id}").attr('src', url_{trailer_web_id});
                }});
'''

# The following creates the 6 modal boxes for the trailers to be displayed in
web_template_modal = '''
    <!-- Modal -->
    <div id={modal_web_id} class="modal fade">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                    <h4 class="modal-title">{movie_title} Trailer</h4>
                </div>
                <div class="modal-body">
                    <iframe id="{trailer_web_id}" width="560" height="315" src="{youtube_URL}" frameborder="0" allowfullscreen></iframe>
                </div>
            </div>
        </div>
    </div>
'''

# The following creates the table in which all the content is filled, the poster, description, rating, and length
web_template_element = '''
    <div class="row" style="background-color: {bgcolor};">
        <div class="col-sm-3" align="center">
            <a href="#"><img src="{poster_image_url}" class="img-thumbnail" alt="poster" width="200" height="260" data-toggle="modal" data-target="#{modal_web_id}"></a>
        </div>
        <div class="content col-sm-9">
            <div class="row">
                <div class="col-sm-12"><h1>{title}</h1></div>
            </div>
            <div class="row">
                <div class="col-sm-12">{storyline}</div>
            </div>
            <div class="row" style="position:absolute; bottom:0px; width: 100%;">
                <div class="col-sm-4">{rating}</div>
                <div class="col-sm-4">{length}</div>
                <div class="col-sm-4"><a href="#" data-toggle="modal" data-target="#{modal_web_id}"><img src="play.png" width="30" height="30">Play Movie Trailer</a></div>
            </div>
        </div>
    </div>
'''

# main() - starts the main function of the program
def main():
    movies = fill_content() # Creates the array with all the movie content

    # The following variables all need to be initialized to '' or 0
    contents = ''
    modal = ''
    script_content = ''
    toggle = 0
    counter = 0

    # Loop through every movie class object in the array movies
    for movie in movies:
        if toggle == 0: # This if statement alternates between two colors for each row
            background_color = "white"
            toggle = 1
        else:
            background_color = "whitesmoke"
            toggle = 0

        # Initialize the dynamic names for the html element ids; The counter increases the index of the name for each movie element
        modal_id = "modal" + str(counter)
        trailer_id = "trailer" + str(counter)

        # The following three lines format the strings, replacing the bracketed variables in the html with the dynamic data from the python code
        contents = contents + web_template_element.format(
            poster_image_url = movie.poster_image_url,
            title = movie.title,
            storyline = movie.storyline,
            bgcolor = background_color,
            modal_web_id = modal_id,
            rating = movie.rating,
            length = movie.length)
        modal = modal + web_template_modal.format(
            modal_web_id = modal_id,
            trailer_web_id = trailer_id,
            movie_title = movie.title,
            youtube_URL = movie.trailer_youtube_url)
        script_content = script_content + modal_script.format(
            modal_web_id = modal_id,
            trailer_web_id = trailer_id)
        
        counter = counter + 1 # Increase the counter by 1, moving onto the next element id

    movie_content = web_template_body.format(movie_content=contents, modal_content=modal)

    # Call the show_webpage function, sending the html text combined and formatted
    show_webpage(web_template_head.format(web_template_modal_script = script_content) + movie_content) 


# create_page(content, filename) - Creates a text file using the content supplied and the filename supplied. 
def create_page(content, filename):
    output = open(filename, "w")
    output.write(content)
    output.close()

# show_webpage(content, filename) - content is the html code of the page to create and the filename is just that, the filename defaults to...
#       index.html is no value is supplied
def show_webpage(webpage_content, filename='index.html'):
    create_page(webpage_content, filename) # Call the function that actually writes the page
    webbrowser.open("file:///" + os.path.abspath(filename))

# Fill_content() - Populates all the data into the class objevt movie
def fill_content():
    avatar = movie.Movie("Avatar", "A company with mineral interests on the planet of Pandora sends an ex-marine on a mission to get to know the ways of the locals to try to find a diplomatic solution to land rights and mineral deposits. Things take a turn when the marine goes rogue and joins the locals in an epic fight for their sacred lands.",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                     "https://youtube.com/embed/cRdxXPV9GNQ",
                         "PG-13", "2h 42min")

    step_brothers = movie.Movie("Step Brothers", "Brennan and Dale are two middle aged men going nowhere. When their parents get married they are forced to become step brothers and move in together. While living together they fight and cause marital problems between their parents. As a result, the two team up to save their parents relationship.",
                                "https://cdn.traileraddict.com/content/columbia-pictures/step_brothers.jpg",
                                "https://www.youtube.com/embed/_0TWeOrIYVI",
                                "R", "1h 38min")

    the_avengers = movie.Movie("The Avengers", "The S.H.I.E.L.D. Agency is tasked with bringing together many superheroes to save the planet from being destroyed by Loki.",
                               "http://i2.wp.com/www.slashfilm.com/wp/wp-content/images/AVG_Payoff_1-Sht_v13.jpg",
                               "https://youtube.com/embed/eOrNdBpGMv8",
                               "PG-13", "2h 23min")

    the_shawshank_redemption = movie.Movie("The Shawshank Redemption", "A successful banker is falsely accused of murder and is imprisoned at Shawkshank. While in prison he finds different ways to cope with being falsely imprisoned and becomes good friends with an inmate named Red.",
                                           "https://images-na.ssl-images-amazon.com/images/I/51SPVi-1rXL._SY450_.jpg",
                                           "https://www.youtube.com/embed/6hB3S9bIaco",
                                           "R", "2h 22min")

    guardians_of_the_galaxy = movie.Movie("Guardians of the Galaxy", "A group of rejects and criminals are forced to work together because of a common business deal. However, they end up teaming up to save the universe from a mad man trying to take it over.",
                                          "http://cdn.collider.com/wp-content/uploads/guardians-of-the-galaxy-movie-poster1.jpg",
                                          "https://www.youtube.com/embed/2XltzyLcu0g",
                                          "PG-13", "2h 1min")

    the_minions_movie = movie.Movie("The Minions Movie", "The Minions are in search of a new master. In their searches they come across a supervillain named Scarlet Overkill and they join her.",
                                    "https://i.pinimg.com/originals/25/21/d6/2521d66145c91e8e49e20b9649e7d4a7.jpg",
                                    "https://www.youtube.com/embed/P9-FCC6I7u0",
                                    "PG", "1h 31min")

    movies = [avatar, step_brothers, the_avengers, the_shawshank_redemption, guardians_of_the_galaxy, the_minions_movie]
    return movies # returns the array movies

main()
