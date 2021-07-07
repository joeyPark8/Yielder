#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

class yielder
{
public:
	vector<vector<int>> scores;
	vector<vector<float>> proportions;
	vector<string> subjects;
	map<string, float> results;

private:
	string scoreFilePath = "data/score.txt";
	string proportionFilePath = "data/proportion.txt";
	string resultFilePath = "data/result.txt";

	vector<string> split(string str) {
		vector<string> splitedString;
		string word;
		int count = 0;
		for (char i : str) {
			count += 1;
			if (i != ' ' && count != str.length()) {
				word += i;
			}
			else {
				if (count == str.length()) word += i;
				splitedString.push_back(word);
				word = "";
			}
		}

		return splitedString;
	}

public:
	void load() {
		ifstream reader;
		
		//���� ���� �ε�
		reader.open(scoreFilePath);
		if (reader.is_open()) {
			string line;
			
			while (getline(reader, line)) {
				vector<string> splited = split(line);

				vector<int> subjectScore;
				for (string i : splited) {
					const char* str = i.c_str();
					int num = atoi(str);

					subjectScore.push_back(num);
				}

				scores.push_back(subjectScore);
			}

			reader.close();
		}

		//���� ���� �ε�
		reader.open(proportionFilePath);
		if (reader.is_open()) {
			string line;

			while (getline(reader, line)) {
				vector<string> splited = split(line);

				vector<float> subjectProportion;
				for (string i : splited) {
					const char* str = i.c_str();
					float num = atoi(str) * 0.01;

					subjectProportion.push_back(num);
				}

				proportions.push_back(subjectProportion);
			}
			
			reader.close();
		}

		//���� ����
		subjects.push_back("����");
		subjects.push_back("����");
		subjects.push_back("����");
		subjects.push_back("����");
		subjects.push_back("����");
		subjects.push_back("�Ⱑ");
		subjects.push_back("����");
		subjects.push_back("�ѹ�");
		subjects.push_back("ü��");
		subjects.push_back("����");
		subjects.push_back("�̼�");

	}

	//���� ���� ����
	void yield() {
		int count = 0;
		while (count < subjects.size()) {
			float finalScore = 0;

			int miniCount = 0;
			while (miniCount < scores[count].size()) {
				int score = scores[count][miniCount];
				float proportion = proportions[count][miniCount];

				finalScore += score * proportion;
				
				miniCount++;
			}

			results.insert(pair<string, float>(subjects[count], finalScore));
			
			count++;
		}
	}

	void save() {
		ofstream writer;

		//��� ����
		writer.open(resultFilePath);
		if (writer.is_open()) {
			for (auto [subject, result] : results) {
				writer << subject << " " << result << endl;
			}

			writer.close();
		}
	}
};

