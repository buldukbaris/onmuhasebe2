// custom.js

function confirmAndMarkAsPaid(satinalmaId) {
    // Kullanıcıya onay al
    var isConfirmed = confirm("Nakit ödeme yapıldı olarak işaretle?");

    // Eğer onay alındıysa
    if (isConfirmed) {
        // Django view'ına AJAX ile istek gönder
        $.ajax({
            url: '/satinalma/mark_as_paid/' + satinalmaId + '/',
            method: 'POST',
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                // Başarıyla işlendiğinde yapılacak işlemler
                alert("Ödeme işlemi başarıyla kaydedildi!");
            },
            error: function (error) {
                // Hata durumunda yapılacak işlemler
                alert("Bir hata oluştu. Lütfen tekrar deneyin.");
            }
        });
    }
}
