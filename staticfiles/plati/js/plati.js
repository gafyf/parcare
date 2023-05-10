const cardNumberInput = document.getElementById("card-number");
const visaIcon = document.getElementById("visa-icon");
const masterIcon = document.getElementById("master-icon");


cardNumberInput.addEventListener("input", function() {
  // Hide both icons
  visaIcon.style.display = "none";
  masterIcon.style.display = "none";

  // Get the input value
  const cardNumber = cardNumberInput.value;

  // Check if it starts with a specific set of numbers to determine the card type
  if (cardNumber.startsWith("4")) {
    visaIcon.style.display = "block";
  } else if (cardNumber.startsWith("51") || cardNumber.startsWith("52") || cardNumber.startsWith("53") || cardNumber.startsWith("54") || cardNumber.startsWith("55")) {
    masterIcon.style.display = "block";
  }
});



// var stripe = Stripe('pk_test_51MU89FAvOfhHjpZGpnJG1XM3ytRhjvEOQpfdc2KVZcWd3A8TeX0BEbUFTH4AZcZNUEolwROAGrc8OnHlV8Q0Y3dA00miJyzuDp');

// var elem = document.getElementById('submit');
// clientsecret = elem.getAttribute('data-secret');

// // Set up Stripe.js and Elements to use in checkout form
// var elements = stripe.elements();
// var style = {
// base: {
//   color: "#000",
//   lineHeight: '2.4',
//   fontSize: '16px'
// }
// };


// var card = elements.create("card", { style: style });
// card.mount("#card-element");

// card.on('change', function(event) {
// var displayError = document.getElementById('card-errors')
// if (event.error) {
//   displayError.textContent = event.error.message;
//   $('#card-errors').addClass('alert alert-info');
// } else {
//   displayError.textContent = '';
//   $('#card-errors').removeClass('alert alert-info');
// }
// });

// var form = document.getElementById('payment-form');

// form.addEventListener('submit', function(ev) {
// ev.preventDefault();

// var custName = document.getElementById("custName").value;
// var custAdd = document.getElementById("custAdd").value;
// var custAdd2 = document.getElementById("custEmail").value;
// var carNr = document.getElementById("carNr").value;
// var custAbb = document.getElementById("custAbb").value;


//   $.ajax({
//     type: "POST",
//     url: 'http://127.0.0.1:8000/clienti/clienti5/<str:pk>/',
//     data: {
//       order_key: clientsecret,
//       csrfmiddlewaretoken: CSRF_TOKEN,
//       action: "post",
//     },
//     success: function (json) {
//       console.log(json.success)

//       stripe.confirmCardPayment(clientsecret, {
//         payment_method: {
//           card: card,
//           billing_details: {
//             address:{
//                 line1:custAdd,
//                 line2:custAdd2
//             },
//             name: custName,
//           },
//         }
//       }).then(function(result) {
//         if (result.error) {
//           console.log('payment error')
//           console.log(result.error.message);
//         } else {
//           if (result.paymentIntent.status === 'succeeded') {
//             console.log('payment processed')
//             // There's a risk of the customer closing the window before callback
//             // execution. Set up a webhook or plugin to listen for the
//             // payment_intent.succeeded event that handles any business critical
//             // post-payment actions.
//             window.location.replace("http://127.0.0.1:8000/parcare/");
//           }
//         }
//       });

//     },
//     error: function (xhr, errmsg, err) {},
//   });



// });