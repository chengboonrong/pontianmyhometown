// Tooltips Initialization
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

const check = () => {
  // get user location
  if(!navigator.geolocation) {
    status.textContent = 'Geolocation is not supported by your browser';
  } else {
    status.textContent = 'Locating…';
    navigator.geolocation.getCurrentPosition(success, error);
  }
}

function success(position) {
  const latitude  = position.coords.latitude;
  const longitude = position.coords.longitude;
  if (latitude - 1.4988958 > 1 || latitude - 1.4988958 < -1  && longitude - 103.3761729 > 1 || longitude - 103.3761729 < -1) {
    console.log("You are not in Pontian area, please come back home >.< "); // send notification if the person is not in Pontian area
    return true;
  }
  else {
    return false;
  }
}

function error() {
  console.log('Unable to retrieve your location');
}

// $('#btn').submit(function(e) {
//   e.preventDefault();
//   // Coding
//   $('#thankModel').modal('toggle'); //or  $('#IDModal').modal('hide');
//   return false;
// });

// if ('serviceWorker' in navigator && 'PushManager' in window) {
//   console.log('Service Worker and Push are supported');

//   navigator.serviceWorker.register('/static/js/sw.js')
//   .then(function(swReg) {
//     console.log('Service Worker is registered', swReg);

//     swRegistration = swReg;
//     askPermission();
//     console.log(Notification.permission);
//   })
//   .catch(function(error) {
//     console.error('Service Worker Error', error);
//   });
// } else {
//   console.warn('Push messaging is not supported');
//   pushButton.textContent = 'Push Not Supported';
// }

// function askPermission() {
//   return new Promise(function(resolve, reject) {
//     const permissionResult = Notification.requestPermission(function(result) {
//       resolve(result);
//     });

//     if (permissionResult) {
//       permissionResult.then(resolve, reject);
//     }
//   })
//   .then(function(permissionResult) {
//     showLocalNotification("From notification", "Hello ...", swRegistration);
//     if (permissionResult !== 'granted') {
//       throw new Error('We weren\'t granted permission.');
//     }
//   });
// }

// const showLocalNotification = (title, body, swRegistration) => {
//   const options = {
//       body,
//       // here you can add more properties like icon, image, vibrate, etc.
//   };
//   swRegistration.showNotification(title, options);
// }