var btn = document.createElement('button');
btn.style.margin = '10px';
btn.innerHTML = '...';
document.body.appendChild(btn);

var lightstatus = "off";
document.body.style.backgroundColor = "black";
btn.innerHTML = 'Switch light on';

function lightswitch() {
    if (lightstatus == "off") {
        btn.innerHTML = "Switch light off";
        lightstatus = "on";
        document.body.style.backgroundColor = "yellow";
        console.log("Light is on")
    } 
    else if (lightstatus == "on") {
        btn.innerHTML = "Switch light on";
        lightstatus = "off";
        document.body.style.backgroundColor = "black";
        console.log("Light is off")
    }
}

btn.onclick = lightswitch