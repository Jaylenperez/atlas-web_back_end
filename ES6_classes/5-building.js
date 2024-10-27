// 5-building.js
class Building {
    constructor(sqft) {
      this._sqft = sqft;
    }
  
    // Getter for sqft
    get sqft() {
      return this._sqft;
    }
  
    // Abstract method to be overridden in subclasses
    evacuationWarningMessage() {
      throw new Error("Class extending Building must override evacuationWarningMessage");
    }
  }
  
  export default Building;
  