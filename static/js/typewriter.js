$(function() {
    var srcText = $(".src").html();
    var i = 0;
    var result = srcText[i];
    setInterval(function() {
            if(i == srcText.length) {
                clearInterval(this);
                return;
            };
            i++;
            result += srcText[i].replace("\n", "<br />");
            $("#target").html( result);
    },
    50); // the period between every character and next one, in milliseonds.
});