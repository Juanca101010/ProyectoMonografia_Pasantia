// Obtener los mensajes de una base de datos o API
const messages = [
    {
      id: 1,
      from: "user1@example.com",
      subject: "Mensaje 1",
      content: "Contenido del mensaje 1"
    },
    {
      id: 2,
      from: "user2@example.com",
      subject: "Mensaje 2",
      content: "Contenido del mensaje 2"
    },
    // ...
  ];
  
  // Obtener los contactos de una base de datos o API
  const contacts = [
    {
      id: 1,
      name: "Usuario 1",
      email: "user1@example.com"
    },
    {
      id: 2,
      name: "Usuario 2",
      email: "user2@example.com"
    },
    // ...
  ];
  
  // Agregar los mensajes a la lista de mensajes
  const messagesList = document.querySelector(".email-messages ul");
  messages.forEach(message => {
    const li = document.createElement("li");
    li.innerHTML = `<strong>${message.from}</strong>: ${message.subject}`;
    messagesList.appendChild(li);
  });
  
  // Agregar los contactos a la lista de contactos
  const contactsList = document.querySelector(".email-contacts ul");
  contacts.forEach(contact => {
    const li = document.createElement("li");
    li.innerHTML = `${contact.name} <${contact.email}>`;
    contactsList.appendChild(li);
  });
  