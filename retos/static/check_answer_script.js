                             $(function () {

                                $('#btnCompare').on('click', function () {
                                    compare();
                                    return false;
                                });

                                function compare() {
                                    $('#divColLeft').empty();
                                    $('#divColRight').empty();

                                    var textOne = $.trim($('#copyArea').val());
                                    var textTwo = $.trim($('#newPasteArea').val());

                                    var TempArr1 = textOne.split(' ');
                                    var TempArr2 = textTwo.split(' ');
                                    var arr1 = [];
                                    for (var i = 0; i < TempArr1.length; i++) {
                                        if (TempArr1[i] !== "" && TempArr1[i] !== null) {
                                            arr1.push(TempArr1[i]);
                                        }
                                    }

                                    var arr2 = [];
                                    for (var i = 0; i < TempArr2.length; i++) {
                                        if (TempArr2[i] !== "" && TempArr2[i] !== null) {
                                            arr2.push(TempArr2[i]);
                                        }
                                    }
                                    var minArrLen = arr1.length < arr2.length ? arr1.length : arr2.length;

                                    for (var x = 0; x < minArrLen; x++) {

                                        var maxCharLen = arr1[x].length > arr2[x].length ? arr1[x].length : arr2[x].length;
                                        for (var y = 0; y < maxCharLen; y++) {
                                            if (arr1[x].charAt(y) == ' ') {
                                                $('#divColLeft').append('<span  class="missing">' + arr2[x].charAt(y) + '</span>');

                                                $('#divColRight').append('<span class="missmatch">' + arr2[x].charAt(y)) + '</span>';
                                            }
                                            else if (arr2[x].charAt(y) == ' ') {
                                                $('#divColLeft').append('<span class="missing">' + arr1[x].charAt(y) + '</span>');

                                                $('#divColRight').append('<span class="missmatch">' + arr1[x].charAt(y)) + '</span>';
                                            } else if (arr1[x].charAt(y) == arr2[x].charAt(y)) {
                                                $('#divColLeft,#divColRight').append(arr1[x].charAt(y));
                                            }
                                            else {
                                                $('#divColLeft').append('<span  class="missmatch">' + arr1[x].charAt(y) + '</span>');
                                                $('#divColRight').append('<span  class="missing">' + arr2[x].charAt(y) + '</span>');
                                            }
                                        }
                                        $('#divColLeft').append(' ');
                                        $('#divColRight').append(' ');
                                    }

                                    if (minArrLen < arr1.length) {
                                        for (var Len=minArrLen; Len < arr1.length; Len++) {
                                            $('#divColLeft').append(arr1[Len])
                                                            .append(' ');
                                        }
                                    } else if (minArrLen < arr2.length) {
                                        for (var Len=minArrLen; Len < arr2.length; Len++) {
                                            $('#divColRight').append( arr2[Len] )
                                                            .append(' ');
                                        }
                                    }
                                }
                            });


  function formExit() {
    document.getElementById("newForm").remove();
  }

  function myFunction(id) {
    if (document.contains(document.getElementById("newForm"))) {
      document.getElementById("newForm").remove();


    }

    var d1 = document.getElementById(id);
    d1.insertAdjacentHTML('afterend',

      '<form id="newForm" class="form-insert py-2" method="post"> \
                <div class="d-flex justify-content-between"><h2>Reply:</h2><div><button type="button" class="btn btn-outline-secondary" onclick="formExit()"">Close</button></div></div> \
                <label for="id_name">Name:</label> \
                <input type="text" name="name" class="col-sm-12" maxlength="50" required="" id="id_name">\
                <select name="parent" class="d-none" id="id_parentt"> \
                <option value="' + id + '" selected="' + id + '"></option> \
                </select> \
                <label for="id_email">Email:</label> \
                <input type="text" name="email" class="col-sm-12" maxlength="254" required="" id="id_email"> \
                <label for="id_content">Content:</label> \
                <textarea name="content" cols="40" rows="5" class="form-control" required id="id_content"></textarea> \
                {% csrf_token %} \
                <button type="submit" class="btn btn-primary btn-lg btn-block">Submit</button> \
              </form>');


    //document.querySelector('#id_parentt [value="' + id + '"]').selected = true;
  }

  $('#myForm').trigger("reset");


