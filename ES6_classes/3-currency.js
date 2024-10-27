export default class Currency {
    constructor(code, name) {
      if (typeof code !== 'string' || code.trim().length === 0) {
        throw new Error('Code must be a non empty string');
      }
      if (typeof name !== 'string' || name.trim().length === 0) {
        throw new Error('Name must be a non empty string');
      }
  
      this._code = code;
      this._name = name;
    }
  
    get code() {
      return this._code;
    }
  
    get name() {
      return this._name;
    }
  
    set code(newCode) {
      if (typeof newCode !== 'string' || newCode.trim().length === 0) {
        throw new Error('Code must be a non empty string');
      }
      this._code = newCode;
    }
  
    set name(newName) {
      if (typeof newName !== 'string' || newName.trim().length === 0) {
        throw new Error('Name must be a non empty string');
      }
      this._name = newName;
    }
  
    displayFullCurrency() {
      return (`${this._name} (${this._code})`);
    }
  }