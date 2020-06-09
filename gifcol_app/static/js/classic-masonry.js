// Get the modal
            var modal{{ forloop.counter }} = document.getElementById("myModal{{ forloop.counter }}");

            // Get the button that opens the modal
            var btn = document.getElementById("myBtn{{ forloop.counter }}");

            // Get the <span> element that closes the modal
            var span = document.getElementsByClassName("close-btn{{ forloop.counter }}")[0];

            // When the user clicks on the button, open the modal
            btn.onclick = function() {
                modal{{ forloop.counter }}.style.display = "block";
            }

            // When the user clicks on <span> (x), close the modal
            span.onclick = function() {
                modal{{ forloop.counter }}.style.display = "none";
            }

            // When the user clicks anywhere outside of the modal, close it
            window.onclick = function(event) {
                if (event.target == modal{{ forloop.counter }}) {
                    modal{{ forloop.counter }}.style.display = "none";
                }
            }