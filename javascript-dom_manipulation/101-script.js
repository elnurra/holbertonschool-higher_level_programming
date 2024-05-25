document.addEventListener('DOMContentLoaded', () => {
  const languageSelect = document.getElementById('language_code');
  const translateButton = document.getElementById('btn_translate');
  const helloDisplay = document.getElementById('hello');

  translateButton.addEventListener('click', () => {
    const selectedLanguageCode = languageSelect.value;
    if (selectedLanguageCode) {
      const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${selectedLanguageCode}`;
      fetch(apiUrl)
        .then(response => response.json())
        .then(data => {

          if (data.hasOwnProperty('hello')) {
            helloDisplay.textContent = data.hello;
          } else {
            helloDisplay.textContent = 'Translation not found.';
          }
        })
        .catch(error => {
          console.error('Error fetching translation:', error);
          helloDisplay.textContent = 'An error occurred.';
        });
    } else {
      helloDisplay.textContent = 'Please select a language.';
    }
  });
});
