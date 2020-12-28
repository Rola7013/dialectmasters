$('textarea').autoResize();

var button = document.getElementById("copy");
var myDiv = document.getElementById("myDiv");

document.getElementById('copy').addEventListener('click', ()=>{
   document.getElementById('copyArea').select();
    document.execCommand('copy');
                            });


                            document.getElementById('paste').addEventListener('click', ()=>{
                                let pasteArea = document.getElementById('pasteArea');

                                pasteArea.value = '';
                                navigator.clipboard.readText()
                                .then((text)=>{
                                    pasteArea.value = text;
                                });

                            });

                            function getChar(event) {
                              // event.which returns the key or mouse button clicked
                              // Return the char if not a special character
                              if (event.which === null) return String.fromCharCode(event.keyCode); // IE
                              else if (event.which !== 0 && event.charCode !== 0) return String.fromCharCode(event.which); // Other Browsers
                              return null; // Special Key Clicked
                            }



                            document.getElementById('pasteArea').onkeyup = function(event) {
                              if (this.value.length === 0) {
                                alert('Empty');
                                // variable resetting here
                              }
                            }


                            function show() {
                                myDiv.style.visibility = "visible";
                            }

                            function hide() {
                                myDiv.style.visibility = "hidden";
                            }

                            function toggle() {
                                if (myDiv.style.visibility === "hidden") {
                                    show();
                                } else {
                                    hide();
                                }
                            }

                            hide();

                            button.addEventListener("click", toggle, false);