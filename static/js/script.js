function preview(input,id){

const file=input.files[0];

if(!file)return;

const reader=new FileReader();

reader.onload=function(e){

const img=document.getElementById(id);

img.src=e.target.result;

img.style.display="block";

}

reader.readAsDataURL(file);

}

document.getElementById("encodeImage").onchange=function(){

preview(this,"encodePreview");

};

document.getElementById("decodeImage").onchange=function(){

preview(this,"decodePreview");

};
