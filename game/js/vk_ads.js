// game/js/vk_ads.js

// Функция для показа рекламы с вознаграждением (Rewarded Video)
function showRewardedVideo() {
  console.log("Attempting to show rewarded video...");
  // Проверяем, доступна ли реклама
  vkBridge.send('VKWebAppCheckNativeAds', { ad_format: 'reward' })
    .then((data) => {
      if (data.result) {
        // Реклама доступна, показываем ее
        return vkBridge.send('VKWebAppShowNativeAds', { ad_format: 'reward' });
      } else {
        // Реклама не найдена, сообщаем об этом
        console.log("No rewarded ad available right now.");
        // Вызываем callback об ошибке в Ren'Py
        if (window.onAdError) {
          window.onAdError("Реклама сейчас недоступна. Попробуйте позже.");
        }
        return Promise.reject("No ad available");
      }
    })
    .then((data) => {
      if (data.result) {
        // Реклама была успешно просмотрена
        console.log("Rewarded ad watched successfully!");
        // Вызываем callback об успехе в Ren'Py для начисления награды
        if (window.onAdSuccess) {
          window.onAdSuccess();
        }
      } else {
        // Пользователь закрыл рекламу, не досмотрев
        console.log("User closed rewarded ad before finishing.");
        if (window.onAdError) {
          window.onAdError("Вы не досмотрели рекламу до конца.");
        }
      }
    })
    .catch((error) => {
      // Обработка других ошибок (например, отказ от показа)
      console.error("Ad showing error:", error);
      if (window.onAdError) {
        let errorMessage = "Произошла ошибка при показе рекламы.";
        if (error.error_data && error.error_data.error_reason) {
            errorMessage = error.error_data.error_reason;
        }
        window.onAdError(errorMessage);
      }
    });
}

// Функция для показа межстраничной рекламы (Interstitial)
function showInterstitial() {
  console.log("Attempting to show interstitial...");
  vkBridge.send('VKWebAppCheckNativeAds', { ad_format: 'interstitial' })
    .then((data) => {
      if (data.result) {
        return vkBridge.send('VKWebAppShowNativeAds', { ad_format: 'interstitial' });
      } else {
        console.log("No interstitial ad available right now.");
        // Для interstitial можно просто ничего не делать, если рекламы нет
        if (window.onInterstitialFinished) {
            window.onInterstitialFinished();
        }
        return Promise.reject("No ad available");
      }
    })
    .then((data) => {
        // Успех или закрытие - в любом случае просто продолжаем игру
        console.log("Interstitial finished.");
        if (window.onInterstitialFinished) {
            window.onInterstitialFinished();
        }
    })
    .catch((error) => {
      console.error("Interstitial error:", error);
      // Даже при ошибке мы должны продолжить игру
      if (window.onInterstitialFinished) {
        window.onInterstitialFinished();
      }
    });
}