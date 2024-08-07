// JavaScript script that fetches from
// https://hellosalut.stefanbohacek.dev/?lang=fr and displays
// the value of hello from that fetch in the HTML tag DIV#hello

$(() => {
    const fetch_url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
    $.get(fetch_url, (data, textStatus) => {
        if (textStatus == "success") {
            $('DIV#hello').text(data.hello);
        }
    });
});
