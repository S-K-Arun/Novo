Dropzone.autoDiscover = false;


const myDropzone = new Dropzone("#my-dropzone",{

            url: "upload/",
            maxFiles: 2,
            maxFilesize: 2,
            acceptedFiles: '.jpg',

})