function admin(){
    
    document.getElementById("right").style.display = "block";
    document.getElementById("right").style.width = "80vw";
    document.getElementById("right").style.display = "70vh";
    document.getElementById("left").style.width = "0vw"
    document.getElementById("patient").style.display = "none"   
    
    setTimeout(tii, 509);

}

function tii(){
    document.getElementById("admin").style.display = "block"  
}

function patient(){
    
    document.getElementById("left").style.display = "block";
    document.getElementById("left").style.width = "80vw";
    document.getElementById("left").style.display = "70vh";
    document.getElementById("right").style.width = "0vw";
    
    document.getElementById("admin").style.display = "none"  
    document.getElementById("right").style.background = "green"  
    setTimeout(ti, 509);
      
}
function ti(){
document.getElementById("patient").style.display = "block" 
}