
# HTML content you want to save

html_content = """

                <!-- 024 Personal Branding -->
                <div class="grid-item branding col-md-4 col-sm-6">
                  <div class="item-wrap">
                     <figure class="">
                        <div class="popup-call">
                           <a href="assets/custom/images/blog/024_influence.jpeg" class="gallery-item"><i class="flaticon-arrows-4"></i></a>
                        </div>
                        <img src="assets/custom/images/blog/thumbs/024_influence.jpeg" class="img-responsive" alt="img03"/>
                        <figcaption>
                           <div class="post-meta"><span>by <a href="#!">Jason Rathgeber</a>,</span> <span>December 16, 2024</span></div>
                           <div class="post-header">
                              <h5><a href="blogpost/blogpost_024_increase_your_impact.html">Scale Your Influence</a></h5>
                           </div>
                           <div class="post-entry">
                              <p>Increase your impact online</p>
                           </div>
                           <div class="post-tag pull-left">
                              <span><a href="#branding" data-filter=".branding">Branding</a>,</span>
                           </div>
                           <div class="post-more-link pull-right"><a href="blogpost/blogpost_024_increase_your_impact.html">More<i class="fa fa-long-arrow-right right"></i></a></div>
                        </figcaption>
                     </figure>
                  </div>
              </div> 

"""

# File path where you want to save the HTML file
file_path = "my_page.html"

# Open the file in write mode and save the HTML content
with open(file_path, "w") as file:
    file.write(html_content)

print(f"HTML file saved as {file_path}")