(function($){
    $.fn.tileslide = function(options){
        if(!options) options = {};
        var default_args = {
            "slide_time":   300,
            "slide_height": 50,
        }
        for(var arg in default_args){
            if(typeof options[arg] == "undefined"){
                options[arg] = default_args[arg];
            }
        }
        var img_height = parseInt($(this).find(".tile_img").css("height"));
        var text_height = parseInt($(this).find(".tile_text").css("height"));
        $(this).hover(function(){
            $(this).css("z-index","100");
            $(this).find(".tile_img").stop().animate({"top":"-"+options["slide_height"]+"px"},options["slide_time"]);
            $(this).find(".tile_text").stop().animate({"top":String(img_height-options["slide_height"])+"px"},options["slide_time"]);
        },function(){
            var tile = this;
            $(tile).css("z-index","99");
            $(this).find(".tile_img").stop().animate({"top":"0px"},options["slide_time"],function(){
                $(tile).css("z-index","1");
            });
            $(this).find(".tile_text").stop().animate({"top":String(img_height-text_height)+"px"},options["slide_time"]);
        });
    };
})(jQuery);
