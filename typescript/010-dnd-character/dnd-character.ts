export class DnDCharacter {

  public strength: number = DnDCharacter.generateAbilityScore();
  public dexterity: number = DnDCharacter.generateAbilityScore();
  public constitution: number = DnDCharacter.generateAbilityScore();
  public intelligence: number = DnDCharacter.generateAbilityScore();
  public wisdom: number = DnDCharacter.generateAbilityScore();
  public charisma: number = DnDCharacter.generateAbilityScore();
  public hitpoints: number = 10 + DnDCharacter.getModifierFor(this.constitution);

  public static rollDie(): number {
    return Math.floor(Math.random() * 6) + 1;
  }

  public static generateAbilityScore(): number {
    const fourDices: number[] = Array(4).fill(0).map(() => DnDCharacter.rollDie());
    return fourDices.reduce((a, b) => a + b, 0) - Math.min(...fourDices);
  }

  public static getModifierFor(abilityValue: number): number {
    return Math.floor((abilityValue - 10) / 2);
  }
}
