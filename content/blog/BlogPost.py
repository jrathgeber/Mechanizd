

def new_post(path, number, slug, key_words, formatted_date):

    html_content = """
        
    
<!DOCTYPE html>
<html lang="en">

   <head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name=viewport content="width=device-width, initial-scale=1">

""" + """

   <title>""" + key_words + """</title>
   <meta name="description" content=""" + key_words + """>
   <meta name="keywords" content=""" + key_words + """>
   <meta name="author" content="Jason Rathgeber">

""" + """

   <!-- CSS -->
   <link href="../assets/vendor/bootstrap/css/bootstrap.min.css"        property='stylesheet' rel="stylesheet" type="text/css" media="screen"/>
   <link href="../assets/vendor/fontawesome/css/font-awesome.min.css"   property='stylesheet' rel="stylesheet" type="text/css" media="screen"/>
   <link href="../assets/vendor/flaticons/flaticon.css"                 property='stylesheet' rel="stylesheet" type="text/css" media="screen"/>
   <link href="../assets/vendor/hover/css/hover-min.css"                property='stylesheet' rel="stylesheet" type="text/css" media="screen"/>
   <link href="../assets/vendor/wow/animate.css"                        property='stylesheet' rel="stylesheet" type="text/css" media="screen"/>
   <link href="../assets/vendor/mfp/css/magnific-popup.css"             property='stylesheet' rel="stylesheet" type="text/css" media="screen"/>
   <link href="../assets/custom/css/style.css"                          property='stylesheet' rel="stylesheet" type="text/css" media="screen"/>

   <style>
      #preloader {
         position: fixed;
         left: 0;
         top: 0;
         z-index: 99999;
         width: 100%;
         height: 100%;
         overflow: visible;
         background: #666666 url("../assets/custom/images/preloader.gif") no-repeat center center; }
   </style>

</head>

<body class="boxed">


<!--Pre-Loader-->
<div id="preloader"></div>

<header>

   <section id="top-navigation" class="container-fluid nopadding">

      <div class="row nopadding ident e-bg-light-texture">

         <!-- Photo -->
         <a href="#!">
            <div class="col-md-5 col-lg-4 vc-photo">&nbsp;</div>
         </a>
         <!-- /Photo -->

         <div class="col-md-7 col-lg-8 vc-name nopadding">
            <!-- Name-Position -->
            <div class="row nopadding name">
               <div class="col-md-10 name-title"><h2 class="font-accident-two-light uppercase">Jason Rathgeber</h2></div>
               <div class="col-md-2 nopadding name-pdf">
                  <a href="https://github.com/jrathgeber" class="hvr-sweep-to-right"><i class="flaticon-download149" title="Download Code"></i></a>
               </div>
            </div>
            <div class="row nopadding position">
               <div class="col-md-10 position-title">

                  <section class="cd-intro">
                     <h4 class="cd-headline clip is-full-width font-accident-two-normal uppercase">
                        <span>The experienced </span>
                        <span class="cd-words-wrapper">
                           <b class="is-visible">Fintec Developer</b>
                           <b>Data Scientist</b>
                           <b>Web Guru</b>
                        </span>
                     </h4>
                  </section>

               </div>
               <div class="col-md-2 nopadding pdf">
                  <a href="https://www.linkedin.com/in/jrathgeber" class="hvr-sweep-to-right"><i class="flaticon-linkedin22" title="My LinkedIn Profile"></i></a>
               </div>
            </div>
            <!-- /Name-Position -->

            <!-- Main Navigation -->
            <ul id="nav" class="row nopadding cd-side-navigation">
               <li class="col-xs-4 col-sm-2 nopadding menuitem green">
                  <a href="../../index.html" class="hvr-sweep-to-bottom"><i class="flaticon-insignia"></i><span>home</span></a>
               </li>
               <li class="col-xs-4 col-sm-2 nopadding menuitem blue">
                  <a href="../resume.html" class="hvr-sweep-to-bottom"><i class="flaticon-graduation61"></i><span>resume</span></a>
               </li>
               <li class="col-xs-4 col-sm-2 nopadding menuitem cyan">
                  <a href="../portfolio.html" class="hvr-sweep-to-bottom"><i class="flaticon-book-bag2"></i><span>portfolio</span></a>
               </li>
               <li class="col-xs-4 col-sm-2 nopadding menuitem orange">
                  <a href="../contacts.html" class="hvr-sweep-to-bottom"><i class="flaticon-placeholders4"></i><span>contacts</span></a>
               </li>
               <li class="col-xs-4 col-sm-2 nopadding menuitem red">
                  <a href="../feedback.html" class="hvr-sweep-to-bottom"><i class="flaticon-earphones18"></i><span>feedback</span></a>
               </li>
               <li class="col-xs-4 col-sm-2 nopadding menuitem yellow">
                  <a href="../blog.html" class="hvr-sweep-to-bottom"><i class="flaticon-pens15"></i><span>blog</span></a>
               </li>
            </ul>
            <!-- /Main Navigation -->

         </div>
      </div>
   </section>

</header>

<!-- Container -->
<div class="content-wrap">

   <div id="blogpost" class="inner-content">

      <section id="page-title" class="inner-section">
         <div class="container-fluid nopadding wow fadeInRight" data-wow-delay="0.4s" data-wow-offset="10">
            <div class="post-meta"><span>by <a href="#!">Jason Rathgeber</a>,</span> <span> """ + formatted_date + """ </span></div>
         </div>
      </section>

      <!-- Blog Block -->
      <section class="inner-section">

         <div class="container-fluid nopadding">

            <!-- Post Content -->
           <article class="post wow fadeInDown" data-wow-delay="0.6s" data-wow-offset="10">

                <div class="article"></div>     
                <div class="lastly"></div>     
                
           </article>

         </div>
         <div class="dividewhite8"></div>

      </section>
      <!-- /Blog Block -->

   </div>

</div>

<footer class="padding-50 e-bg-light-texture">
   <div class="container-fluid nopadding">
      <div class="row wow fadeInDown" data-wow-delay=".2s" data-wow-offset="10">
         <div class="col-md-3">
            <h4 class="font-accident-two-normal uppercase">Jason Rathgeber</h4>
            <p class="inline-block">
               AI Automation, FinTech, BI Guru, Web Developer, Trading Strategy Design
            </p>
            <div class="divider-dynamic"></div>
         </div>
         <div class="col-md-3 cv-link">
            <h4 class="font-accident-two-normal uppercase">Download cv</h4>
            <div class="dividewhite1"></div>
            <a href="http://www.jasonrathgeber.com/docs/JasonRathgeber_CV.pdf">1 Page</a>
            <a href="http://www.jasonrathgeber.com/docs/JasonRathgeber_Fixed_Income_Developer.pdf">Developer</a>
            <a href="http://www.jasonrathgeber.com/docs/JasonRathgeber_BI_Architect.pdf">BI Architect</a>
            <div class="divider-dynamic"></div>
         </div>
         <div class="col-md-3">
            <h4 class="font-accident-two-normal uppercase">Subscribe</h4>
            <div class="dividewhite1"></div>
            <input>
            <!--<p>Lorem ipsum dolor sit amet...</p>-->
            <div class="divider-dynamic"></div>
         </div>
         <div class="col-md-3">
            <h4 class="font-accident-two-normal uppercase">Follow me at</h4>
            <div class="inline-block"><a href="https://www.facebook.com/jrathgeber"><i class="flaticon-facebook45"></i></a></div>
            <div class="inline-block"><a href="https://twitter.com/jprathgeber"><i class="flaticon-twitter39"></i></a></div>
            <div class="inline-block"><a href="https://www.pinterest.com/jasonrathgeber/"><i class="flaticon-pinterest28"></i></a></div>
            <div class="inline-block"><a href="https://www.linkedin.com/in/jrathgeber"><i class="flaticon-linkedin22"></i></a></div>
            <div class="inline-block"><a href="https://www.quantconnect.com/u/16951"><i class="flaticon-odnolassniki2"></i></a></div>
            <div class="inline-block"><a href="http://www.stocktwits.com/J_R"><i class="flaticon-vk6"></i></a></div>
            <div class="divider-dynamic"></div>
         </div>
      </div>
      <div class="dividewhite1"></div>
      <div class="row wow fadeInDown" data-wow-delay=".4s" data-wow-offset="10">
         <div class="col-md-12 copyrights">
            <p>© 2024 Jason Rathgeber.</p>
         </div>
      </div>
   </div>
</footer>

<div id="image-cache" class="hidden"></div>

<!-- JS -->
<script src="../assets/vendor/jquery/js/jquery-2.2.0.min.js"            type="text/javascript"></script>
<script src="../assets/vendor/bootstrap/js/bootstrap.min.js"            type="text/javascript"></script>
<script src="../assets/vendor/imagesloaded/js/imagesloaded.pkgd.min.js" type="text/javascript"></script>
<script src="../assets/vendor/isotope/js/isotope.pkgd.min.js"           type="text/javascript"></script>
<script src="../assets/vendor/mfp/js/jquery.magnific-popup.min.js"      type="text/javascript"></script>
<script src="../assets/vendor/circle-progress/circle-progress.js"       type="text/javascript"></script>
<script src="../assets/vendor/waypoints/waypoints.min.js"               type="text/javascript"></script>
<script src="../assets/vendor/anicounter/jquery.counterup.min.js"       type="text/javascript"></script>
<script src="../assets/vendor/wow/wow.min.js"                           type="text/javascript"></script>
<script src="../assets/vendor/pjax/jquery.pjax.js"                      type="text/javascript"></script>
<script src="https://maps.google.com/maps/api/js"                    type="text/javascript"></script>
<script src="../assets/custom/js/custom.js"                             type="text/javascript"></script>

<script>

 $(function () {
    $.get("./Articles/article_""" + number + """_""" + slug + """.html", function (data) {$(".article").append(data); });
 });

 $(function () {
    $.get("./Articles/lastly.html", function (data) {$(".lastly").append(data); });
 });


 </script>

 
</body>
</html>
    
    
    
    """

    # File path where you want to save the HTML file
    file_path = path + "blogpost_" + number + "_" + slug + ".html"

    # Open the file in write mode and save the HTML content
    with open(file_path, "w") as file:
        file.write(html_content)

    print(f"HTML file saved as {file_path}")