import QuestoesService
import QuestoesServiceWithOpenGL as questoesGL


translacoes: dict = {'translacao01': [
                                        [1, 0, 0, 3],
                                        [0, 1, 0, 5],
                                        [0, 0, 1, 0],
                                        [0, 0, 0, 1]
                  ], 'translacao02': [
                                        [3, 0, 0, 0],
                                        [0, 4, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 1]
                  ]
                }

QuestoesService.Questao01.resolucao(5,5)
QuestoesService.Questao02.resolucao([3, 2], [6, 8])
QuestoesService.Questao03.resolucao([3, 2], [6, 8])
QuestoesService.Questao04.resolucao([3, 2], [6, 8], [7, 3])
QuestoesService.Questao05.resolucao([3, 2, 0], [6, 8, 0], [7, 3, 0], translacoes['translacao01'])
QuestoesService.Questao06.resolucao([3, 2, 0], [6, 8, 0], [7, 3, 0], translacoes['translacao02'])


questoesGL.Questao01.resolucao(5, 5)
questoesGL.Questao02.resolucao([3, 2], [6, 8])
questoesGL.Questao03.resolucao([3, 2], [6, 8])
questoesGL.Questao04.resolucao([3, 2], [6, 8], [7, 3])
questoesGL.Questao05.resolucao([3, 2, 0], [6, 8, 0], [7, 3, 0], translacoes['translacao01'])
questoesGL.Questao06.resolucao([3, 2, 0], [6, 8, 0], [7, 3, 0], translacoes['translacao02'])
