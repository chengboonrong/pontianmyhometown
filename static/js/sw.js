self.addEventListener('activate', async () => {
    // This will be called only once when the service worker is activated.
    console.log('service worker activate')
})
  
function showNotification() {
    Notification.requestPermission(function(result) {
      if (result === 'granted') {
        console.log("YESS YES !!!!!!")
        navigator.serviceWorker.ready.then(function(registration) {
          registration.showNotification('Vibration Sample', {
            body: 'Buzz! Buzz!',
          });
        });
      }
    });
}

askPermission();
showNotification();