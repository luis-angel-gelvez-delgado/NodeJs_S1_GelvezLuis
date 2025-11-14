class Notification{
    send(message){
        throw new error("metodo send() debera ser implementado en las subclases");
    }

}

class EmailNotification extends Notification{
    send(message){
        console.log(`enviando sms: ${message}`);
    }
}

class PushNotification extends Notification{
    send(message){
        console.log(`enviando notificacion push: ${message}`);
    }
}

module.exports = {
    Notification,
    EmailNotification,
    SMSNotification,
    
}