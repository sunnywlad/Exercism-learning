function isAQuestion(message: string): boolean {
  const cleanedMessage = message.trim();
  return cleanedMessage.charAt(cleanedMessage.length - 1) === '?';
}

function isAYell(message: string): boolean {
  return (message.toUpperCase() === message) &&
  (/[a-zA-Z]+/.test(message));
}

function isSilence(message: string): boolean {
  return message.trim() === '';
}

export function hey(message: string): string {
  const question = isAQuestion(message);
  const yell = isAYell(message);
  if (question && yell) {
    return 'Calm down, I know what I\'m doing!';
  } else if (yell) {
    return 'Whoa, chill out!';
  } else if (question) {
    return 'Sure.';
  } else if (isSilence(message)) {
    return 'Fine. Be that way!'
  } else {
    return 'Whatever.';
  }
}
