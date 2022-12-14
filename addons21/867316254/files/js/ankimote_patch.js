
/* ------------------------------------------------------------------------------
#
# MIT License
#
# Copyright (c) 2021 nogira
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# --------------------------------------------------------------------------- */


function main() {
    const off_template = "Ankimote ✘";
    const selector = `[title="Shortcut: Ctrl+Shift+R"]`;
    const id = "#ankimote";

    $(selector).prop("id", "ankimote");

    const off = $(id).text() === off_template;

    // replace text with svg
    const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path d="M288 200a56 56 0 1 0 56 56 56 56 0 0 0-56-56zM64 256a214.3 214.3 0 0 1 55.42-144.06c5.59-6.22 4.91-15.74-1.08-21.59L96 68.53a16.41 16.41 0 0 0-23.56 1C25.59 121 0 186.56 0 256s25.59 135 72.44 186.52a16.41 16.41 0 0 0 23.56 1l22.34-21.82c6-5.85 6.67-15.37 1.08-21.59A214.3 214.3 0 0 1 64 256zm134.27-87.63l-22.76-22.23a16.44 16.44 0 0 0-24 1.31 168.77 168.77 0 0 0 0 217.1 16.44 16.44 0 0 0 24 1.31l22.76-22.22a15.12 15.12 0 0 0 1.45-20.32 107.39 107.39 0 0 1 0-134.64 15.11 15.11 0 0 0-1.45-20.31zm305.29-98.89a16.41 16.41 0 0 0-23.56-1l-22.34 21.87c-6 5.85-6.67 15.37-1.08 21.59a214.95 214.95 0 0 1 0 288.12c-5.59 6.22-4.91 15.74 1.08 21.59L480 443.47a16.41 16.41 0 0 0 23.56-1C550.41 391 576 325.44 576 256s-25.59-135-72.44-186.52zm-79.1 78a16.44 16.44 0 0 0-24-1.31L377.7 168.4a15.11 15.11 0 0 0-1.45 20.31 107.39 107.39 0 0 1 0 134.64 15.12 15.12 0 0 0 1.45 20.32l22.76 22.22a16.44 16.44 0 0 0 24-1.31 168.77 168.77 0 0 0 0-217.1z" /></svg>`;
    $(id).html(svg);

    if (off) {
        $(id + " > svg").css("opacity", 0.3)
    }
};


// this is called everytime the ankimote button changes because ankimote calls 
// a page reload

$(document).ready(() => {

    // check if ankimote is present
    if (document.querySelector(`[title="Shortcut: Ctrl+Shift+R"]`) !== null) {
            //            function   ms
            window.setTimeout(main, 100)
    }

})