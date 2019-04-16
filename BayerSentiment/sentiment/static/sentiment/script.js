function myFunction1() {
              document.getElementById("myDropdown1").classList.toggle("show");
            }
            
       
            
            function myFunction2() {
              document.getElementById("myDropdown2").classList.toggle("show");
            }
            
            window.onclick = function(event) {
              if (!event.target.matches('.dropbtn2')) {
                var dropdowns = document.getElementsByClassName("dropdown-content2");
                var i;
                for (i = 0; i < dropdowns.length; i++) {
                  var openDropdown = dropdowns[i];
                  if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show'); 
                  }
                }
              }
            }
            var header = document.getElementById("btn-group1");
            var btns = header.getElementsByClassName("btn1");
            for (var i = 0; i < btns.length; i++) {
                btns[i].addEventListener("click", function() {
                    var current = document.getElementsByClassName("active");
                    current[0].className = current[0].className.replace(" active", "");
                    this.className += " active";
                });
            }
            var header1 = document.getElementById("btn-group2");
            var btns1 = header1.getElementsByClassName("btn2");
            for (var j = 0; j < btns1.length; j++) {
                btns1[j].addEventListener("click", function() {
                    var current1 = document.getElementsByClassName("active");
                    current1[0].className = current1[0].className.replace(" active", "");
                    this.className += " active";
                });
            }
