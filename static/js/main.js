
window.addEventListener("DOMContentLoaded", (event) => {
    document.getElementById('type').addEventListener('change', function () {
        if (document.getElementById('type').value == "Ресторан"){
          document.getElementById('hd1').style.display = "block";
          document.getElementById('hd2').style.display = "none";
          document.getElementById('hd3').style.display = "none";
        }

        if (document.getElementById('type').value == "Культурное место"){
          document.getElementById('hd2').style.display = "block";
          document.getElementById('hd1').style.display = "none";
          document.getElementById('hd3').style.display = "none";
        }

        if (document.getElementById('type').value == "Развлечения"){
          document.getElementById('hd3').style.display = "block";
          document.getElementById('hd2').style.display = "none";
          document.getElementById('hd1').style.display = "none";
        }
    });

})