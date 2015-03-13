function ran_col() { //function name
    var color = '#'; // hexadecimal starting symbol
    var letters = ['F64747','663399','E4F1FE','22313F','86E2D5','BDC3C7','03C9A9','1BBC9B']; //Set your colors here
    color += letters[Math.floor(Math.random() * letters.length)];
    document.getElementById('rand_back_color').style.background = color;
}