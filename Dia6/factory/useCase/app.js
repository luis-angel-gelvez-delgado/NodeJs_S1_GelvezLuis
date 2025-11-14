class EmailNotification {
    send(message) {
      console.log(`[EMAIL] Enviando email: ${message}`);
    }
  }
  
  class SMSNotification {
    send(message) {
      console.log(`[SMS] Enviando SMS: ${message}`);
    }
  }
  
  class PushNotification {
    send(message) {
      console.log(`[PUSH] Enviando notificación push: ${message}`);
    }
  }
  
  // Cliente
  function sendNotification(type, message) {
    let notifier;
  
    if (type === "email") {
      notifier = new EmailNotification();
    } else if (type === "sms") {
      notifier = new SMSNotification();
    } else if (type === "push") {
      notifier = new PushNotification();
    } else {
      throw new Error("Tipo de notificación no soportado");
    }
  
    notifier.send(message);
  }
  
  // Ejemplos de uso
  sendNotification("email", "Bienvenido a la plataforma");
  sendNotification("sms", "Tu código es 123456");
  sendNotification("push", "Tienes una nueva tarea");