//speechToText.js
//converts speech to text using SpeechRecogniton API
//Developer: Shavon Thadani
//23/08/'21

//Initialize SpeechRecogniton object
try {
  var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  var recognition = new SpeechRecognition();
}
catch(e) {
  console.error(e);
  $('.app').hide();
}

//Declare variables and access html elements
var noteTextarea = $('#note');
var noteContent = '';
//continue recording voice
recognition.continuous = true;

recognition.onresult = function(event) {

  // event is a SpeechRecognitionEvent object.
  // It holds all the lines we have captured so far.
  // We only need the current one.
  var current = event.resultIndex;

  // Get a transcript of what was said.
  var transcript = event.results[current][0].transcript;
  //Concatenate what is being said to textarea
    noteContent += transcript;
    noteTextarea.val(noteContent);

};

recognition.onerror = function(event) {
  if(event.error == 'no-speech') {
    instructions.text('No speech was detected. Try again.');
  };
}

/*-----------------------------
      App buttons and input
------------------------------*/
//If start button is clicked
$('#start-record-btn').on('click', function(e) {
  if (noteContent.length) {
    noteContent += ' ';
  }
  recognition.start();

});

//if pause button is clicked
$('#pause-record-btn').on('click', function(e) {
  recognition.stop();

});

// Sync the text inside the text area with the noteContent variable.
noteTextarea.on('input', function() {
  noteContent = $(this).val();
})
