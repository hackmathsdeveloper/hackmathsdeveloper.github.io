
Here are **100 more**, numbered 101–200. This set emphasizes factorial quotients, binomial/Stirling transforms, probability, analytic identities, and deeper number-theoretic structure. Falling and rising factorial identities connect directly to permutations and binomial coefficients. [en.wikipedia](https://en.wikipedia.org/wiki/Falling_and_rising_factorials)

## Factorial quotients and binomials

101. \(\displaystyle \frac{(n+r)!}{n!}=(n+1)(n+2)\cdots(n+r)\)

102. \(\displaystyle \frac{n!}{(n-r)!}=n(n-1)\cdots(n-r+1)\)

103. \(\displaystyle \binom nr=\frac{n^{\underline r}}{r!}\), where \(n^{\underline r}\) is a falling factorial.

104. \(\displaystyle \binom{n+r-1}{r}=\frac{n^{\overline r}}{r!}\), where \(n^{\overline r}\) is a rising factorial.

105. Binomial symmetry: \(\displaystyle \binom nr=\binom n{n-r}\).

106. Pascal recurrence: \(\displaystyle \binom nr=\binom{n-1}{r}+\binom{n-1}{r-1}\).

107. Absorption identity: \(\displaystyle r\binom nr=n\binom{n-1}{r-1}\).

108. Complementary absorption: \(\displaystyle (n-r)\binom nr=n\binom{n-1}{r}\).

109. Hockey-stick identity: \(\displaystyle \sum_{k=r}^{n}\binom kr=\binom{n+1}{r+1}\).

110. Alternating hockey-stick identity: \(\displaystyle \sum_{k=r}^{n}(-1)^k\binom kr=(-1)^n\binom{n-1}{r-1}\).

111. Binomial inversion: if \(\displaystyle b_n=\sum_{k=0}^{n}\binom nk a_k\), then \(\displaystyle a_n=\sum_{k=0}^{n}(-1)^{n-k}\binom nk b_k\).

112. The number of \(r\)-element subsets of an \(n\)-set is \(\binom nr\).

113. The number of ordered \(r\)-tuples of distinct elements from an \(n\)-set is \(n!/(n-r)!\).

114. The number of \(r\)-element multisets drawn from \(n\) types is \(\binom{n+r-1}{r}\).

115. The number of nonnegative solutions of \(x_1+\cdots+x_n=r\) is \(\binom{n+r-1}{r}\).

116. The number of positive solutions of \(x_1+\cdots+x_n=r\) is \(\binom{r-1}{n-1}\).

117. \(\displaystyle \binom{-n}{r}=(-1)^r\binom{n+r-1}{r}\).

118. The generalized binomial series is \(\displaystyle (1+x)^\alpha=\sum_{r\ge0}\binom{\alpha}{r}x^r\).

119. For integer \(n\), \(\displaystyle \binom n0=\binom nn=1\).

120. The largest binomial coefficient in row \(n\) occurs at \(r=\lfloor n/2\rfloor\) or \(r=\lceil n/2\rceil\).

121. The adjacent ratio is \(\displaystyle \frac{\binom n{r+1}}{\binom nr}=\frac{n-r}{r+1}\).

122. Therefore, binomial coefficients increase up to the middle of Pascal’s triangle and then decrease symmetrically.

123. \(\displaystyle \sum_{r=0}^{n}r(r-1)\binom nr=n(n-1)2^{n-2}\).

124. \(\displaystyle \sum_{r=0}^{n}r^2\binom nr=n(n+1)2^{n-2}\).

125. \(\displaystyle \sum_{r=0}^{n}(-1)^r r\binom nr=0\) for \(n\ge2\).

126. \(\displaystyle \sum_{r=0}^{n}(-1)^r r^n\binom nr=(-1)^n n!\).

127. More generally, \(\displaystyle \sum_{r=0}^{n}(-1)^{n-r}\binom nr r^m=0\) for \(m<n\).

128. For \(m=n\), that same finite-difference sum equals \(n!\).

129. \(\displaystyle \binom{2n}{n}\) is always even for \(n\ge1\).

130. \(\displaystyle \binom{2n}{n}\sim \frac{4^n}{\sqrt{\pi n}}\).

## Stirling, partitions, and permutations

131. The Stirling number of the second kind satisfies
\[
S(n,k)=\frac1{k!}\sum_{j=0}^{k}(-1)^{k-j}\binom kj j^n.
\]

132. \(S(n,k)\) counts partitions of an \(n\)-element set into exactly \(k\) nonempty unlabeled blocks.

133. \(S(n,k)\) obeys \(\displaystyle S(n,k)=kS(n-1,k)+S(n-1,k-1)\).

134. The number of surjections from an \(n\)-set onto a \(k\)-set is \(k!S(n,k)\).

135. The number of injective maps from an \(r\)-set to an \(n\)-set is \(n!/(n-r)!\).

136. The number of all functions from an \(n\)-set to a \(k\)-set is \(k^n\).

137. Inclusion–exclusion gives surjections as
\[
\sum_{j=0}^{k}(-1)^j\binom kj(k-j)^n.
\]

138. The unsigned Stirling number \(\left[{n\atop k}\right]\) counts permutations of \(n\) objects with exactly \(k\) cycles.

139. These satisfy
\[
\left[{n\atop k}\right]=\left[{n-1\atop k-1}\right]+(n-1)\left[{n-1\atop k}\right].
\]

140. \(\displaystyle \sum_{k=0}^{n}\left[{n\atop k}\right]=n!\).

141. The signed Stirling numbers expand falling factorials:
\[
x^{\underline n}=\sum_{k=0}^{n}s(n,k)x^k.
\]

142. The second-kind Stirling numbers invert that relation:
\[
x^n=\sum_{k=0}^{n}S(n,k)x^{\underline k}.
\]

143. The two Stirling-number matrices are inverses:
\[
\sum_{k} s(n,k)S(k,m)=\delta_{nm}.
\]

144. Bell numbers satisfy \(\displaystyle B_n=\sum_{k=0}^{n}S(n,k)\).

145. \(B_n\) counts all set partitions of an \(n\)-element set.

146. Dobinski’s formula is
\[
B_n=\frac1e\sum_{k=0}^{\infty}\frac{k^n}{k!}.
\]

147. The exponential generating function for Bell numbers is \(\exp(e^x-1)\).

148. The number of involutions satisfies \(\displaystyle I_n=I_{n-1}+(n-1)I_{n-2}\).

149. An involution is a permutation equal to its own inverse.

150. The number of even permutations of \(n\) objects is \(n!/2\), for \(n\ge2\).

151. The number of odd permutations is also \(n!/2\), for \(n\ge2\).

152. The signed sum of all permutations is zero for \(n\ge2\).

153. The determinant expansion of an \(n\times n\) matrix has \(n!\) permutation terms.

154. The permanent expansion also has \(n!\) terms, but without permutation signs.

155. The number of ways to arrange a multiset with multiplicities \(a_1,\ldots,a_t\) is
\[
\frac{(a_1+\cdots+a_t)!}{a_1!\cdots a_t!}.
\]

## Probability and analysis

156. A uniformly random permutation of \(n\) elements has probability \(1/n!\) of being any particular permutation.

157. The probability that a random permutation is a derangement is \(!n/n!\).

158. This derangement probability tends to \(1/e\).

159. The expected number of fixed points in a random permutation is \(1\).

160. The expected number of cycles in a random permutation is
\[
H_n=1+\frac12+\cdots+\frac1n.
\]

161. The probability that a particular \(r\)-subset appears in a uniformly random ordering in a prescribed relative order is \(1/r!\).

162. A Poisson random variable satisfies
\[
\Pr(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}.
\]

163. The Poisson probabilities sum to \(1\) because of the exponential series.

164. Taylor’s formula uses factorial normalization:
\[
f(x)=\sum_{n\ge0}\frac{f^{(n)}(a)}{n!}(x-a)^n.
\]

165. \(\displaystyle \frac{d^n}{dx^n}x^m=\frac{m!}{(m-n)!}x^{m-n}\) for \(m\ge n\).

166. \(\displaystyle \frac{d^n}{dx^n}x^n=n!\).

167. The sine series is
\[
\sin x=\sum_{n\ge0}(-1)^n\frac{x^{2n+1}}{(2n+1)!}.
\]

168. The cosine series is
\[
\cos x=\sum_{n\ge0}(-1)^n\frac{x^{2n}}{(2n)!}.
\]

169. The hyperbolic sine series is
\[
\sinh x=\sum_{n\ge0}\frac{x^{2n+1}}{(2n+1)!}.
\]

170. The hyperbolic cosine series is
\[
\cosh x=\sum_{n\ge0}\frac{x^{2n}}{(2n)!}.
\]

171. Gamma recurrence: \(\Gamma(z+1)=z\Gamma(z)\).

172. Gamma reflection formula:
\[
\Gamma(z)\Gamma(1-z)=\frac{\pi}{\sin(\pi z)}.
\]

173. Gamma duplication formula:
\[
\Gamma(z)\Gamma\left(z+\tfrac12\right)=2^{1-2z}\sqrt{\pi}\,\Gamma(2z).
\]

174. The beta function is
\[
B(x,y)=\frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}.
\]

175. For integers \(m,n\ge0\),
\[
B(m+1,n+1)=\frac{m!n!}{(m+n+1)!}.
\]

## Number theory and advanced patterns

176. The Wilson quotient for prime \(p\) is
\[
W_p=\frac{(p-1)!+1}{p},
\]
which is always an integer. [en.wikipedia](https://en.wikipedia.org/wiki/Wilson's_theorem)

177. A Wilson prime is a prime \(p\) satisfying \((p-1)!\equiv-1\pmod{p^2}\). [math.dartmouth](https://math.dartmouth.edu/~carlp/PDF/paper111.pdf)

178. The \(p\)-adic valuation of a binomial coefficient is
\[
v_p\!\left(\binom nr\right)=v_p(n!)-v_p(r!)-v_p((n-r)!).
\]

179. Kummer’s theorem: this valuation equals the number of carries when adding \(r\) and \(n-r\) in base \(p\).

180. \(\binom nr\) is odd exactly when every binary \(1\)-bit of \(r\) is also a \(1\)-bit of \(n\).

181. The number of odd entries in row \(n\) of Pascal’s triangle is \(2^{s_2(n)}\), where \(s_2(n)\) is the binary digit sum of \(n\).

182. \(\displaystyle \gcd(n!,n!+1)=1\).

183. \(\displaystyle \gcd(n!,n!-1)=1\).

184. \(\displaystyle \gcd(n!, (n+1)!)=n!\).

185. \(\displaystyle \operatorname{lcm}(n!,(n+1)!)=(n+1)!\).

186. The divisor count of \(n!\) is
\[
\tau(n!)=\prod_{p\le n}\bigl(v_p(n!)+1\bigr).
\]

187. The divisor-sum function of \(n!\) is
\[
\sigma(n!)=\prod_{p\le n}\frac{p^{v_p(n!)+1}-1}{p-1}.
\]

188. Euler’s totient of \(n!\) is
\[
\varphi(n!)=n!\prod_{p\le n}\left(1-\frac1p\right).
\]

189. The least common multiple \(\operatorname{lcm}(1,\ldots,n)\) consists of the largest prime powers \(p^a\le n\).

190. Its logarithm is the Chebyshev function:
\[
\log\operatorname{lcm}(1,\ldots,n)=\sum_{p^a\le n}\log p.
\]

191. \(\displaystyle \binom nr\) is integral because every prime valuation in its factorial quotient is nonnegative.

192. The factorial sequence is divisible by every fixed positive integer from some point onward.

193. For any fixed modulus \(m\), \(n!\equiv0\pmod m\) for all \(n\ge m\).

194. Consequently, the sequence \(n!\bmod m\) eventually becomes permanently zero.

195. \(\displaystyle \frac{1}{n!}\) decreases faster than any geometric sequence \(c^{-n}\) for fixed \(c>0\).

196. The series \(\sum_{n\ge0}1/n!\) converges absolutely.

197. The series \(\sum_{n\ge0}n!/x^n\) diverges for every fixed finite nonzero \(x\).

198. The ordinary generating function \(\sum_{n\ge0}n!x^n\) therefore has radius of convergence \(0\).

199. The exponential generating function of the factorial sequence is
\[
\sum_{n\ge0}\frac{n!}{n!}x^n=\frac1{1-x}.
\]

200. Factorials act as the normalization that turns many combinatorial counting sequences into well-behaved exponential generating functions.
