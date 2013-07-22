$(document).ready(function(){
    $('#map-continents').cssMap({
        agentsListId : '#addresses',
        // optional: fade in/fade out delay in miliseconds;
        agentsListSpeed : 500,
        // optional: show and hide agent/address on hover;
        agentsListOnHover : true,
        size : 960
    });
});