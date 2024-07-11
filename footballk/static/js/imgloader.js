document.addEventListener('DOMContentLoaded', (event) => {
  const images = document.querySelectorAll('img');
  let loadedCount = 0;

  images.forEach((img) => {
    img.addEventListener('load', () => {
      loadedCount++;
      if (loadedCount === images.length) {
        console.log('Iamgenes cargadas');
        const spinner = document.getElementById('loading')
        spinner.style.display = 'none'
      }
      else {
        const spinner = document.getElementById('loading')
        spinner.style.display = 'absolute'
      }
    });
  });
});