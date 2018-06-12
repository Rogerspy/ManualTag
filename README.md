<link href='http://fonts.googleapis.com/css?family=Joti+One' rel='stylesheet' type='text/css'>  
<div class="shadow effect1">  
  <img src="https://github.com/Rogerspy/ManualTag/blob/master/img/1.PNG" alt="" />  
  <style>
        /*===========.shadow统一设置================*/  
        .shadow{  
          width: 960px;  
          height:540px;  
          margin:100px auto;  
          position: relative;  
          border: 0px solid #000;  
        }  
        .shadow img{  
          position: relative;  
          width:100%;  
          z-index: 2;  
        }   
        .effect1:before,.effect1:after{  
          content:"";  
          position: absolute;  
          width: 50%;  
          height: 35%;  
          max-width: 300px;  
          max-height: 50px;  
          background-color: #000;  
          z-index:1;  
          box-shadow: 0 15px 10px rgba(0,0,0,.5);  
        }  
        .effect1:before{  
          left:10px;  
          bottom:10px;  
          /*transform:rotate(-3deg);*/  
          transform:skewY(-3deg);  
        }  
        .effect1:after{  
          right:10px;  
          bottom:10px;  
          /*transform:rotate(3deg);*/  
          transform:skewY(3deg);  
        }  
  </style>
</div>  


# ManualTag
Manual text data tag tool.
